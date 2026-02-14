
from flask import Flask,render_template,request
from flask_mail import Mail,Message
import os,zipfile,yt_dlp,time
from pydub import AudioSegment


app = Flask(__name__)

# ===== EMAIL CONFIG =====
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='pallikamalhotra@gmail.com',
    MAIL_PASSWORD='kgbivchydahrlsoa'
)

mail = Mail(app)

os.makedirs("audios", exist_ok=True)

# ===== MASHUP FUNCTION =====
def mashup(singer, n, duration):

    # Clear old audios safely
    for f in os.listdir("audios"):
        try:
            os.remove("audios/" + f)
        except:
            pass

    ydl_opts = {
    'format': 'bestaudio[ext=m4a]/bestaudio/best',
    'outtmpl': 'audios/%(id)s.%(ext)s',
    'noplaylist': True,
    'quiet': False,
    'retries': 10,
    'fragment_retries': 10,
    'socket_timeout': 30,
    'overwrites': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128'
    }]
}



    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch{n}:{singer}"])
        time.sleep(2)


    final = AudioSegment.empty()

    for f in os.listdir("audios"):
        audio = AudioSegment.from_mp3("audios/" + f)

        final += audio[:duration * 1000]

    final.export("output.mp3", format="mp3")

    with zipfile.ZipFile("result.zip", "w") as z:
        z.write("output.mp3")




# ===== WEB ROUTE =====
@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        singer = request.form["singer"]
        videos = int(request.form["videos"])   # ANY NUMBER
        duration = int(request.form["duration"])
        email = request.form["email"]

        mashup(singer, videos, duration)

        msg = Message("Your Mashup is Ready!",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[email])

        msg.attach("result.zip", "application/zip", open("result.zip","rb").read())
        mail.send(msg)
        msg.html = f"""
<div style="font-family:Arial; background:#f5eee6; padding:25px; border-radius:12px;">
  <h2 style="color:#6f4e37;">🎧 Mashup Studio</h2>

  <p style="color:#4b2e1e; font-size:16px;">
    Hi there! <br><br>
    Your custom mashup has been created successfully 🎶
  </p>

  <div style="background:#e6d3b3; padding:15px; border-radius:10px;">
    <p style="color:#4b2e1e;"><strong>Singer:</strong> {singer}</p>
    <p style="color:#4b2e1e;"><strong>Videos used:</strong> {videos}</p>
    <p style="color:#4b2e1e;"><strong>Clip duration:</strong> {duration} seconds</p>
  </div>

  <p style="color:#4b2e1e; margin-top:20px;">
    Your mashup is attached as a ZIP file. Enjoy the music! 🎵
  </p>

  <hr style="border:none; border-top:1px solid #b08968; margin:20px 0;">

  <p style="color:#6f4e37;">
    — Mashup Studio <br>
    <strong>Made by Pallika Malhotra</strong>
  </p>
</div>
"""


        return "🎉 Mashup sent to your email!"

    return render_template("index.html")


app.run(debug=True)


