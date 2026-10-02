"""Builds the static pages for www.dodill.com.

Shared header and footer live here so every page stays identical.
Run:  python3 build.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
EMAIL = "dabaroody@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/danbaroody"
GITHUB = "https://github.com/hazard224"


def page(path, title, desc, body, current=None, scripts=""):
    depth = 0 if path.endswith(".html") else (path.count("/") + 1 if path else 0)
    up = "../" * depth
    if path == "404.html":
        up = "/"
    nav = [("Portfolio", "portfolio/index.html"), ("Tools", "tools/index.html"), ("Resume", "resume/index.html")]
    nav_html = "\n".join(
        f'      <a class="nav-{name.lower()}" href="{up}{href}"{" aria-current=\"page\"" if name == current else ""}>{name}</a>'
        for name, href in nav
    )
    slug = (current or ("home" if path == "" else "plain")).lower()
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="preload" href="{up}fonts/caprasimo-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
  <script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
  <link rel="stylesheet" href="{up}css/site.css">
  <script src="{up}js/theme.js"></script>
  <script src="{up}js/accordion.js" defer></script>
  <script src="{up}js/analytics.js" data-privacy="{up}privacy.html"></script>
</head>
<body class="page-{slug}">
  <a class="skip" href="#content">Skip to content</a>

  <header class="wrap site-head{' site-head-home' if slug == 'home' else ''}">
{'' if slug == 'home' else f"""    <a class="name" href="{up}index.html">Dan Baroody</a>
"""}    <nav aria-label="Primary">
{nav_html}
      <button class="theme-toggle" type="button" aria-label="Switch theme">
        <svg class="icon-moon" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <svg class="icon-sun" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.2 5.2l1.8 1.8M17 17l1.8 1.8M5.2 18.8 7 17M17 7l1.8-1.8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <span class="theme-word">Dark</span>
      </button>
    </nav>
  </header>

  <main id="content">
{body}
  </main>

  <footer class="wrap site-foot">
    <ul class="foot-links">
      <li><a href="mailto:{EMAIL}">Email</a></li>
      <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
      <li><a href="{GITHUB}">GitHub</a></li>
      <li><a href="{up}resume/index.html">Resume</a></li>
    </ul>
    <p><a href="{up}privacy.html">Privacy</a></p>
  </footer>
{scripts}</body>
</html>
"""
    out = ROOT / path / "index.html" if path else ROOT / "index.html"
    if path.endswith(".html"):
        out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out.relative_to(ROOT))


# ---------- Home ----------
home = f"""    <section class="wrap hero" id="hero">
      <h1>Dan Baroody <span class="title">Problem Solver</span></h1>
      <p class="lede">
        <span class="redline gap" aria-hidden="true"><span class="num">48</span></span>
        Solving problems is my love language and my passion. There is nothing better than helping others achieve their dreams and goals.
        <span class="redline measure" aria-hidden="true"><span class="num">544</span></span>
      </p>
    </section>

    <section class="wrap home-doors" aria-label="Sections">
      <ul class="doors">
        <li><a href="portfolio/index.html"><span class="door-name">Portfolio</span><span class="door-desc">Problems people had, and what I made to solve each one: product screens, a design system, a website redesign, and more.</span></a></li>
        <li><a href="tools/index.html"><span class="door-name">Tools</span><span class="door-desc">Free tools for artists and designers: Creative Spark, the Image Grid Tool and the Color Palette Maker.</span></a></li>
        <li><a href="resume/index.html"><span class="door-name">Resume</span><span class="door-desc">Experience, education and skills, with a PDF to download.</span></a></li>
      </ul>
    </section>

    <section class="wrap about" id="about" aria-labelledby="about-title">
      <h2 class="section-title" id="about-title">About</h2>
      <div>
        <p>I live and work in Elmira, New York. Every job starts the same way: I listen until I understand the problem, then I make what solves it. Over the years that has been dashboards for analysts, a website for prospective students, ads on a newspaper deadline, and small tools of my own.</p>
        <p>I work in Figma and Adobe Creative Cloud, write HTML and CSS, and build my own tools when the right one doesn't exist.</p>
      </div>
    </section>"""
hero_script = """  <script>
    (document.fonts ? document.fonts.ready : Promise.resolve()).then(function () {
      document.getElementById('hero').classList.add('ready');
    });
  </script>
"""
page("", "Dan Baroody, Problem Solver",
     "Dan Baroody, problem solver. Solving problems is his love language and his passion. Portfolio, tools and resume. Elmira, New York.",
     home, scripts=hero_script)

# ---------- Portfolio (solutions log from the earlier draft) ----------
src = (ROOT.parent / "portfolio" / "index.html").read_text()
a = src.index('    <section class="wrap solutions"')
b = src.index("    </section>", a) + len("    </section>")
log = src[a:b]
log = log.replace('src="images/', 'src="../images/').replace('srcset="images/', 'srcset="../images/')
log = log.replace('<h2 class="section-title" id="solutions-title">Solutions</h2>\n        <p>', '<h2 class="section-title" id="solutions-title">Solutions</h2>\n        <p>')
import re as _re
log = _re.sub(r'\s*<div class="solutions-head">.*?</div>', '', log, flags=_re.S)
log = log.replace('aria-labelledby="solutions-title"', 'aria-label="Problems and solutions"')
portfolio = f"""    <section class="wrap page-head">
      <h1>Portfolio</h1>
      <p>Each line is a problem someone had. Open it to see what I made.</p>
      <p class="note">Client names and figures in the Salient screens are placeholders.</p>
    </section>

{log}"""
page("portfolio", "Portfolio, Dan Baroody",
     "Problems people had, and what Dan Baroody made to solve each one.",
     portfolio, current="Portfolio")

# ---------- Tools ----------
def tool(name, href, img, w, h, alt, desc, cls="shot"):
    return f"""      <article class="project">
        <div class="project-text">
          <h2 class="tool-name"><a href="../{href}">{name}</a></h2>
          <p>{desc}</p>
          <ul class="links"><li><a href="../{href}">Open {name}</a></li></ul>
        </div>
        <figure class="project-media {cls}">
          <a href="../{href}" tabindex="-1" aria-hidden="true"><img src="../images/dodill/{img}.webp" srcset="../images/dodill/{img}@2x.webp 2x" width="{w}" height="{h}" loading="lazy" alt=""></a>
        </figure>
      </article>"""

tools = f"""    <section class="wrap page-head">
      <h1>Tools</h1>
      <p>Small tools I built for artists and designers, under the dodill name. They're free, and everything runs in your browser. Nothing you upload leaves your computer.</p>
    </section>

    <section class="wrap tools-list" aria-label="Tools">
{tool("Creative Spark", "Prompt-maker/creative-spark.html", "creative-spark", 1440, 900, "",
      "Sometimes creativity needs a spark. Two random words, and a refresh button (or the spacebar) for more. Use them to start a story, a sketch, a poem or a conversation.")}
{tool("Image Grid Tool", "Image-grid/image-grid.html", "image-grid", 1440, 1662, "",
      "Upload an image, set the canvas size in inches and DPI, position the image, then lay a grid over it with your own rows, columns, line color and weight. Save the result and print it.", "shot tall")}
{tool("Color Palette Maker", "Color-palette/palette-maker.html", "palette-maker", 1440, 900, "",
      "Generate a palette at random or extract one from an uploaded image. Lock the colors you like, regenerate the rest, and export in HEX, RGB or HSL.")}
    </section>"""
page("tools", "Tools, Dan Baroody",
     "Free browser tools for artists and designers: Creative Spark, Image Grid Tool and Color Palette Maker.",
     tools, current="Tools")

# ---------- Resume (text from Dan's resume; phone left off the public copy) ----------
def job(title, org, dates, bullets):
    lis = "\n".join(f"            <li>{b}</li>" for b in bullets)
    return f"""        <div class="job">
          <h3>{title}</h3>
          <p class="meta">{org}, {dates}</p>
          <ul>
{lis}
          </ul>
        </div>"""

jobs = "\n".join([
    job("UX &amp; UI Product Designer", "Salient, Big Flats, New York", "Jul 2014 – Present", [
        "Led UX and UI design for a suite of enterprise business intelligence applications, building the reporting and dashboard interfaces clients use to read performance and trend data.",
        "Contributed to the internal marketing team on web content, digital advertising, and email campaigns, and assisted in the redesign and rebuild of the company website while helping guide its digital marketing goals.",
        "Serve as the in-house technical guide for email content, advising the development team on template structure and build requirements.",
        "Built and maintained design systems and component libraries, enforcing brand and layout consistency across client-facing platforms.",
        "Translated complex data concepts into clear, accessible language and visuals for non-technical audiences.",
        "Conducted usability research and user testing, synthesizing findings into recommendations that shaped ongoing product decisions.",
        "Managed concurrent deliverables across departments, working with business and development teams to keep projects on schedule.",
    ]),
    job("Director of Digital Content and Design", "Elmira College, Elmira, New York", "Feb 2008 – Jul 2014", [
        "Originated every one of Elmira College's social media channels, launching and running the institution's first Facebook, Twitter, YouTube, and Instagram presences and building each audience from zero.",
        "Independently directed the full redevelopment and public launch of Elmira College's website, owning content strategy and coordinating internal departments and outside vendors through launch.",
        "Published and maintained web content for departments across the institution in the college's content management system, keeping public-facing pages current.",
        "Built the email marketing templates and oversaw campaigns running from student recruitment through alumni donations.",
        "Wrote, edited, and designed print and digital publications including viewbooks, brochures, newsletters, and event materials.",
        "Prepared press releases, public statements, and crisis communications for release through digital, social, and print channels.",
    ]),
    job("Creative Director", "inCommand Technologies, Corning, New York", "Aug 2006 – Mar 2008", [
        "Designed and built client-facing websites using a proprietary content management system, HTML, and CSS, managing end-to-end delivery for multiple clients at once.",
        "Created email marketing templates, campaign content, and digital advertising for clients including Pyrex and World Kitchen.",
    ]),
    job("Graphic Designer", "Elmira Star-Gazette, Elmira, New York", "Sep 2005 – Aug 2006", [
        "Designed and produced print advertising in a high-volume, deadline-driven newsroom, managing 75+ ads and supporting assets each daily production cycle.",
        "Led the department's transition from film-based to fully digital desktop production, rapidly mastering new tools under pressure.",
    ]),
])

def skills(head, items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"<h3>{head}</h3><ul>{lis}</ul>"

resume = f"""    <section class="wrap page-head">
      <h1>Dan Baroody</h1>
      <p class="print-contact">Elmira, New York &nbsp; {EMAIL} &nbsp; linkedin.com/in/danbaroody &nbsp; www.dodill.com</p>
      <ul class="resume-actions">
        <li><a href="Dan-Baroody-Resume.pdf" download>Download PDF</a></li>
        <li><a href="mailto:{EMAIL}">Email</a></li>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
      </ul>
    </section>

    <section class="wrap resume">
      <p class="resume-summary">I am the person you call when something is complicated, behind, or falling apart. I organize, I problem-solve, and I bring a creative eye to everything I touch. Nearly two decades of doing exactly that across communications, design, and operations, and I always strive to leave everything I touch in a better place than I found it.</p>
      <div class="resume-grid">
        <div>
          <h2>Experience</h2>
{jobs}
        </div>
        <aside>
          <div class="side-block">
            <h2>Education</h2>
            <h3>Bachelor of Fine Arts, Graphic Design</h3>
            <p>SUNY Oswego, 2002 – 2005</p>
            <h3>Associate of Arts, Art Studies</h3>
            <p>Corning Community College, 1999 – 2002</p>
          </div>
          <div class="side-block">
            <h2>Skills</h2>
            {skills("Digital Marketing", ["Website content management", "Email campaigns", "Content strategy", "Social media platforms", "Digital advertising"])}
            {skills("Web &amp; Technical", ["HTML &amp; CSS", "Email template build", "CMS platforms", "Google Analytics", "Responsive layout", "Figma &amp; Adobe XD", "Usability testing"])}
            {skills("Content", ["Copywriting &amp; editing", "Press materials", "Newsletters", "Photography &amp; video", "Digital publications"])}
            {skills("Tools", ["Adobe Creative Suite", "Canva", "Microsoft Office Suite", "Google Workspace", "Claude &amp; ChatGPT"])}
          </div>
        </aside>
      </div>
    </section>"""
page("resume", "Resume, Dan Baroody",
     "Resume of Dan Baroody: UX and UI product design, digital content, and communications. Elmira, New York.",
     resume, current="Resume")

# ---------- Privacy (original policy text, restyled) ----------
p_src = (ROOT / "privacy.src.html").read_text()
page("privacy.html", "Privacy policy, Dan Baroody", "How www.dodill.com uses analytics.", p_src)

# ---------- 404 ----------
page("404.html", "Page not found, Dan Baroody", "Page not found.",
     """    <section class="wrap page-head">
      <h1>Not found</h1>
      <p>There's no page at this address. Try the <a href="/portfolio/index.html">portfolio</a>, the <a href="/tools/index.html">tools</a> or the <a href="/">home page</a>.</p>
    </section>""")
