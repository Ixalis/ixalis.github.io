"""Build the photo-free, navy two-column application CV."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[1]
for name,file in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold')
NAVY=HexColor('#082f46'); INK=HexColor('#202d35'); MUTED=HexColor('#53636d')
PALE=HexColor('#f1f4f5'); RULE=HexColor('#d7dfe3'); WHITE=HexColor('#ffffff')
W,H=595.28,841.89
c=canvas.Canvas(str(ROOT/'Le_Tien_Phat_CV.pdf'),pagesize=(W,H))
c.setTitle('Lê Tiến Phát - Computer Engineering CV');c.setAuthor('Lê Tiến Phát')
# Quiet neutral panels and a restrained angled navy identity block.
c.setFillColor(PALE);c.rect(0,0,194,H,fill=1,stroke=0)
c.setFillColor(HexColor('#f5f6f7'));c.rect(194,H-174,W-194,174,fill=1,stroke=0)
c.setFillColor(NAVY)
p=c.beginPath();p.moveTo(0,H);p.lineTo(215,H);p.lineTo(191,H-231);p.curveTo(190,H-243,183,H-248,171,H-249);p.lineTo(0,H-263);p.close();c.drawPath(p,fill=1,stroke=0)
c.rect(0,0,W,7,fill=1,stroke=0)

def para(text,x,y,width,size=9.1,leading=13.5,color=INK,bold=False,gap=6):
    st=ParagraphStyle('p',fontName='Bold' if bold else 'Body',fontSize=size,leading=leading,textColor=color)
    q=Paragraph(text,st);_,ht=q.wrap(width,H);q.drawOn(c,x,y-ht);return y-ht-gap

def section(text,x,y,width):
    y=para(text,x,y,width,size=10.2,leading=14,color=NAVY,bold=True,gap=7)
    c.setStrokeColor(RULE);c.setLineWidth(.6);c.line(x,y,x+width,y)
    return y-12

def bullet(text,y):
    c.setFillColor(NAVY);c.circle(226,y-6,1.5,fill=1,stroke=0)
    return para(text,234,y,333,size=9,leading=13.5,gap=7)

# Reading order: identity and contact, sidebar, then professional detail.
y=H-32
y=para('Lê Tiến<br/>Phát',28,y,154,size=24,leading=29,color=WHITE,bold=True,gap=10)
y=para('Computer Engineering<br/>Embedded systems &amp; IoT',28,y,155,size=9.1,leading=14,color=HexColor('#dbe8ef'),gap=16)
for text in [
 'Ho Chi Minh City, Vietnam',
 '<link href="mailto:letienphatwork@gmail.com" color="#ffffff">letienphatwork@gmail.com</link>',
 '<link href="https://ixalis.github.io/" color="#ffffff">ixalis.github.io</link>',
 '<link href="https://github.com/Ixalis" color="#ffffff">github.com/Ixalis</link>',
 '<link href="https://www.linkedin.com/in/letienphatwork/" color="#ffffff">LinkedIn / letienphatwork</link>'
]: y=para(text,28,y,150,size=7.6,leading=12,color=WHITE,gap=4)
assert y>H-249, 'Identity overflows its navy panel'

y=H-288
y=section('EDUCATION',28,y,139)
y=para('Computer Engineering',28,y,139,size=9.3,leading=14,bold=True)
y=para('Ho Chi Minh City University of Technology',28,y,139,size=9,leading=13)
y=para('HCMUT, VNU-HCM<br/>2022 - 2026',28,y,139,size=8.3,leading=13,color=MUTED)
y=para('Studies completed.<br/>Diploma pending.',28,y,139,size=8.3,leading=13,color=MUTED,gap=22)
y=section('TECHNICAL SKILLS',28,y,139)
for title,detail in [
 ('Programming','C/C++ · Python · SQL'),
 ('Embedded &amp; IoT','ESP32-S3 · Raspberry Pi<br/>Tasmota · RS485/Modbus<br/>MQTT'),
 ('Tools &amp; testing','Git · Linux · Pytest<br/>Node-RED · Grafana<br/>Fault injection<br/>Troubleshooting'),
 ('Analysis','Signal processing<br/>Model evaluation<br/>Technical documentation')
]:
 y=para(title,28,y,139,size=8.8,leading=13,bold=True,gap=3)
 y=para(detail,28,y,139,size=8.3,leading=13,color=MUTED,gap=12)
y=para('Communication',28,y,139,size=8.8,leading=13,bold=True,gap=3)
y=para('English communication<br/>Technical reporting',28,y,139,size=8.3,leading=13,color=MUTED)
assert y>35, 'Sidebar overflows'

x=222; width=345;y=H-32
y=para('PROFILE',x,y,width,size=10.2,leading=14,color=NAVY,bold=True,gap=10)
y=para('Computer Engineering studies completed at HCMUT; diploma pending. Internship experience in IoT device integration, firmware troubleshooting and monitoring systems, complemented by academic work in anomaly detection and edge deployment.',x,y,width,size=9,leading=14,gap=8)
y=para('Open to entry-level embedded, testing, manufacturing technology and technical implementation roles.',x,y,width,size=8.5,leading=13,color=MUTED)
assert y>H-164,'Profile overflows'
y=H-197
y=section('PROFESSIONAL EXPERIENCE',x,y,width)
y=para('IoT Development Intern',x,y,width,size=11,leading=15,bold=True,gap=4)
y=para('Lotus Viet Nam Electronic Service - Trading -<br/>Manufacturing Co., Ltd. | Jun - Aug 2025',x,y,width,size=8.2,leading=12,color=MUTED,gap=10)
y=bullet('Integrated ESP32-S3 controllers and environmental sensors into a monitoring pipeline using MQTT, Node-RED and Grafana.',y)
y=bullet('Developed custom Tasmota drivers for RS485/Modbus devices; troubleshot communication, configuration and hardware-integration faults.',y)
y=bullet('Tested continuous operation and sensor-data stability; documented configurations and troubleshooting procedures.',y)
y=section('ACADEMIC &amp; INDEPENDENT PROJECTS',x,y-13,width)
y=para('SCADA / ICS Anomaly Detection<br/>with Edge Deployment',x,y,width,size=10.8,leading=15,bold=True,gap=4)
y=para('Academic capstone | HCMUT | 2026',x,y,width,size=8.2,leading=12,color=MUTED,gap=10)
y=bullet('Built a configurable signal simulator with replay and fault injection for repeatable anomaly-detection experiments.',y)
y=bullet('Deployed an anomaly-detection model with TensorFlow Lite on Raspberry Pi and evaluated an Isolation Forest on ESP32-S3 using emlearn.',y)
y=bullet('Investigated preprocessing and false-alert issues; compared detection performance, inference latency and hardware constraints.',y)
y=para('DeskFlow',x,y-9,width,size=10.8,leading=15,bold=True,gap=4)
y=para('Workspace booking and pricing | Independent project | 2026',x,y,width,size=8.2,leading=12,color=MUTED,gap=6)
y=bullet('Built a FastAPI/SQLAlchemy backend and TypeScript client; implemented automated tests and investigated booking, timezone and revenue-rounding defects.',y)
y=para('<link href="https://github.com/Ixalis/Deskflow" color="#082f46">github.com/Ixalis/Deskflow</link>',x,y,width,size=8,leading=12,color=NAVY)
assert y>34, f'Main column overflows: {y}'
c.save()
print('Created',ROOT/'Le_Tien_Phat_CV.pdf','; main column bottom',round(y))
