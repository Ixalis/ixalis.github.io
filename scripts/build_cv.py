from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

root=Path(__file__).resolve().parents[1]
for name,file in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold')
ink=HexColor('#18212c');blue=HexColor('#153ae8');grey=HexColor('#526174')
styles={
 'name':ParagraphStyle('name',fontName='Bold',fontSize=23,leading=29,textColor=ink,spaceAfter=4),
 'tag':ParagraphStyle('tag',fontName='Bold',fontSize=10,leading=14,textColor=blue,spaceAfter=6),
 'contact':ParagraphStyle('contact',fontName='Body',fontSize=8.5,leading=13,textColor=grey),
 'body':ParagraphStyle('body',fontName='Body',fontSize=9,leading=13,textColor=ink,spaceAfter=5),
 'section':ParagraphStyle('section',fontName='Bold',fontSize=10,leading=14,textColor=blue,spaceBefore=11,spaceAfter=6),
 'title':ParagraphStyle('title',fontName='Bold',fontSize=9.5,leading=13,textColor=ink,spaceAfter=3),
 'meta':ParagraphStyle('meta',fontName='Body',fontSize=8.5,leading=12,textColor=grey,spaceAfter=5),
 'bullet':ParagraphStyle('bullet',fontName='Body',fontSize=9,leading=12.5,textColor=ink,leftIndent=9,firstLineIndent=-9,spaceAfter=4)
}
story=[]
def add(text,style='body'):story.append(Paragraph(text,styles[style]))
def bullet(text):add('- '+text,'bullet')
add('Lê Tiến Phát','name')
add('COMPUTER ENGINEERING | EMBEDDED SYSTEMS &amp; IoT','tag')
add('Ho Chi Minh City, Vietnam | <link href="mailto:letienphatwork@gmail.com">letienphatwork@gmail.com</link>','contact')
add('<link href="https://ixalis.github.io/">ixalis.github.io</link> | <link href="https://github.com/Ixalis">github.com/Ixalis</link> | <link href="https://www.linkedin.com/in/letienphatwork/">linkedin.com/in/letienphatwork</link>','contact')
story.extend([Spacer(1,9),HRFlowable(width='100%',thickness=1,color=blue),Spacer(1,9)])
add('Computer Engineering studies completed at HCMUT; diploma pending. Hands-on internship experience in IoT device integration, firmware troubleshooting and monitoring systems, complemented by academic work in anomaly detection and edge deployment. Seeking entry-level embedded, testing, manufacturing technology or technical implementation roles.')
add('PROFESSIONAL EXPERIENCE','section')
add('IoT Development Intern | Lotus Vietnam','title')
add('Lotus Viet Nam Electronic Service - Trading - Manufacturing Co., Ltd. | Jun - Aug 2025','meta')
bullet('Integrated ESP32-S3 controllers and environmental sensors into a monitoring pipeline using MQTT, Node-RED and Grafana.')
bullet('Developed custom Tasmota drivers for RS485/Modbus devices; troubleshot communication, configuration and hardware-integration faults.')
bullet('Tested continuous operation and sensor-data stability; documented device configurations and troubleshooting procedures for repeatable deployment.')
add('ACADEMIC &amp; INDEPENDENT PROJECTS','section')
add('SCADA / ICS Anomaly Detection with Edge Deployment','title')
add('Academic capstone | HCMUT | 2026','meta')
bullet('Built a configurable signal simulator with replay and fault injection to support repeatable anomaly-detection experiments.')
bullet('Deployed an anomaly-detection model with TensorFlow Lite on Raspberry Pi and evaluated an Isolation Forest on ESP32-S3 using emlearn.')
bullet('Investigated preprocessing and false-alert issues; compared detection performance, inference latency and hardware constraints, and documented findings.')
story.append(Spacer(1,4))
add('DeskFlow | Workspace Booking and Pricing Platform','title')
add('Independent project | 2026 | github.com/Ixalis/Deskflow','meta')
bullet('Built a FastAPI/SQLAlchemy backend and TypeScript client; implemented automated tests and investigated booking, timezone and revenue-rounding defects.')
add('TECHNICAL SKILLS','section')
add('<b>Programming:</b> C/C++, Python, SQL<br/><b>Embedded &amp; IoT:</b> ESP32-S3, Raspberry Pi, Tasmota, RS485/Modbus, MQTT<br/><b>Tools &amp; testing:</b> Git, Linux, Node-RED, Grafana, Pytest, fault injection, troubleshooting<br/><b>Analysis &amp; communication:</b> Signal processing, model evaluation, technical documentation, English communication')
add('EDUCATION','section')
add('Computer Engineering | Ho Chi Minh City University of Technology','title')
add('HCMUT, VNU-HCM | 2022 - 2026 | Studies completed; diploma pending.','meta')
SimpleDocTemplate(str(root/'Le_Tien_Phat_CV.pdf'),pagesize=(595.28,841.89),rightMargin=40,leftMargin=40,topMargin=34,bottomMargin=30,title='Lê Tiến Phát - Computer Engineering CV',author='Lê Tiến Phát').build(story)
print(root/'Le_Tien_Phat_CV.pdf')
