from pathlib import Path
from html import escape
import json
p=Path(__file__).resolve().parent.parent
p.mkdir(exist_ok=True)
data=json.loads((Path(__file__).resolve().parent/'content.json').read_text())
nav=[('about','About me'),('','Home'),('projects','Projects'),('skills','Skills'),('experience','Experience'),('articles','Articles/Theses')]
def intro(title):return f'<section class="page-intro"><h1>{title}<span class="green">.</span></h1></section>'
def img(src,alt):
 placeholder=not src
 src=src or 'assets/image-placeholder.png'
 return f'<div class="thumb real-thumb{ " placeholder-thumb" if placeholder else ""}"><img src="/{src}" alt="{escape(alt) if not placeholder else ""}" loading="lazy"></div>'
contact='<div class="contact-links"><a href="/assets/emmanuel-echefu-cv.pdf" target="_blank" rel="noopener">View CV <span>↗</span></a><a href="mailto:eman.echefu@gmail.com">Email <span>↗</span></a><a href="https://www.linkedin.com/in/emmanuel-echefu-28482b37a/" target="_blank" rel="noopener">LinkedIn <span>↗</span></a></div>'
home='<section class="hero"><h1><span class="personal-name">Emmanuel Echefu<span class="green">.</span></span><span class="portfolio-word"><span class="outline">Portfolio</span><span class="portfolio-hue" aria-hidden="true">Portfolio</span></span></h1><div class="hero-bottom">'+contact+'</div></section><section class="updates"><div class="section-head"><div><h2>Selected Recents/Highlights<span class="green">.</span></h2></div></div>'
for label,link,image,title,desc in [('PROJECT','/projects/#rsvp-reader','assets/rsvp-reading-tool.png','RSVP Reading Interface','A web-based reading tool with adjustable presentation speed and fixed focal-character alignment.'),('THESIS','/articles/#rsvp-thesis','assets/rsvp-thesis-thumbnail.png','RSVP: Reading, Comprehension & Attention','An investigation into RSVP research and the design of a web-based reading interface.'),('PROJECT','/projects/#stock-forecast','assets/project1.png','Neural Stock Forecasting','An interactive Streamlit app built with LSTM and GRU networks.')]:
 home+=f'<a class="update" href="{link}"><span class="update-preview"><span class="update-image"><img src="/{image}" alt="" loading="lazy"></span><span class="date">{label}</span></span><div><h3>{title}</h3><p>{desc}</p></div><span class="round-arrow">↗</span></a>'
home+='</section>'
about='<section class="page-intro about-intro"><h1>About me<span class="green">.</span></h1></section>'+'''<section class="about-grid"><figure><img class="portrait" src="/assets/emmanuel-echefu-portrait.png" alt="Portrait of Emmanuel Echefu" width="1254" height="1254"></figure><div><h2>HELLO, I’M<br>EMMANUEL ECHEFU</h2><p>I’m a computer science student at the University of Nottingham, with a strong interest in artificial intelligence and robotics.</p><p>Alongside my studies, I enjoy researching and writing about developments in technology and computer science. I also build small programming projects to explore new ideas.</p><p>Away from coding, you’ll find me playing competitive TEKKEN, basketball, or table tennis.</p><div class="about-facts"><div><small>STUDYING</small><p>Computer Science<br>University of Nottingham</p></div><div><small>INTERESTS</small><p>AI & robotics<br>Software development</p></div></div><a class="text-link" href="/assets/emmanuel-echefu-cv.pdf" target="_blank" rel="noopener">View my CV ↗</a></div></section>'''
projects=intro('Projects')+'<section class="card-grid projects-grid">'
for item in data['PROJECTS']:
 tags=' · '.join(item['skills'][:4])
 badge='<span class="pinned-tag">Pinned</span>' if item.get('pinned') else '<span class="pinned-tag new-tag">New</span>' if item.get('new') else ''
 projects+=f'<article class="card project-card" id="{escape(item["id"])}">{badge}{img(item.get("image"),item["title"]+" project preview")}<div class="card-body"><h2>{escape(item["title"])}</h2><p>{escape(item["summary"])}</p><p class="tags">{escape(tags)}</p><a class="text-link" href="{escape(item["link"])}" target="_blank" rel="noopener">{escape(item["action"])} ↗</a></div></article>'
projects+='</section>'
skills=intro('Skills')+'<section class="skills-grid">'
for i,category in enumerate(data['SKILL_CATEGORIES']):
 skills+=f'<article class="skill-group"><h2>{escape(category["category"])}</h2><div class="chips">'+''.join('<span>'+escape(item['name'])+'</span>' for item in category['items'])+'</div></article>'
skills+='</section>'
experience=intro('Experience')+'<section class="card-grid experience-grid">'
roles=[('a2dominion','DB','Database Work Experience','A2Dominion','Worked with Microsoft Dynamics on data management, reporting, and query-based searches. Observed technical team coordination and Agile workflows.'),('escape-studios','VFX','Computer Graphics Work Experience','Escape Studios','Used After Effects, Maya, and Nuke for visual effects, developing skills in VFX integration and project management.'),('nottingham','CS','Computer Science Student','University of Nottingham','Building foundations in software engineering, algorithms, databases, and computer systems through programming projects and team coursework.')]
for i,(key,mark,title,org,desc) in enumerate(roles):
 experience+=f'<article class="card" id="{key}">{img(data['EXPERIENCE'][i].get('image'),org+' thumbnail')}<div class="card-body"><h2>{title}</h2><p class="organization">{org}</p><p>{desc}</p><div class="chips">'+''.join('<span>'+escape(skill)+'</span>' for skill in data['EXPERIENCE'][i]['skills'])+'</div></div></article>'
experience+='</section>'
articles=intro('Articles/<wbr>Theses')+'<section class="article-list"><article class="article-row" id="rsvp-thesis"><div><p class="eyebrow">INDEPENDENT THESIS · 2026 · PDF</p><h2>Rapid Serial Visual Presentation: An Investigation into Reading, Comprehension, Attention and Web-Based Implementation</h2><p>A literature-informed investigation of RSVP and the design of a web-based reading tool. Examines reader control, comprehension, and attention through interface analysis, a proposed evaluation methodology, and a clearly labelled simulated worked example.</p></div><a class="text-link" href="/assets/rsvp-thesis.pdf" target="_blank" rel="noopener">Read thesis (PDF) ↗</a></article></section>'


for route,body in [('',home),('about',about),('projects',projects),('skills',skills),('experience',experience),('articles',articles)]:
 links=''.join(f'<a href="/{r+chr(47) if r else ""}" '+('aria-current="page"' if r==route else '')+f'>{n}</a>' for r,n in nav)
 html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{dict(nav)[route]} — Emmanuel Echefu</title><meta name="description" content="Emmanuel Echefu — Computer Science student at the University of Nottingham. Projects in AI, software development, and web technologies."><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Crect width='40' height='40' rx='9' fill='%23f4a6a6'/%3E%3Ctext x='6' y='28' font-size='23' font-family='monospace'%3E/n%3C/text%3E%3C/svg%3E"><link rel="stylesheet" href="/style.css"><script src="/app.js" defer></script></head><body><a class="skip" href="#main">Skip to content</a><header><button class="menu" aria-expanded="false" aria-controls="nav">Menu +</button><nav id="nav">{links}</nav></header><main id="main">{body}</main><footer><a class="brand" href="/">Emmanuel Echefu</a><p>© 2026 Emmanuel Echefu</p><a href="/about/">About me ↗</a></footer><dialog id="modal"><button class="close" aria-label="Close dialog">×</button><div id="modal-content"></div></dialog></body></html>'''
 d=p/route;d.mkdir(exist_ok=True);(d/'index.html').write_text(html)
