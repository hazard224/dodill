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
  <link rel="icon" href="{up}favicon.ico" sizes="any">
  <link rel="icon" href="{up}favicon-32.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Dan Baroody">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://www.dodill.com/{'' if path in ('', ) else (path if path.endswith('.html') else path + '/')}">
  <meta property="og:image" content="https://www.dodill.com/images/og.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preload" href="{up}fonts/caprasimo-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
  <script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
  <link rel="stylesheet" href="{up}css/site.css">
  <script src="{up}js/theme.js"></script>
  <script src="{up}js/accordion.js" defer></script>
  <script src="{up}js/modal.js" defer></script>
  <script src="{up}js/sort.js" defer></script>
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

    <section class="wrap featured" aria-labelledby="featured-title">
      <div class="featured-head">
        <h2 class="section-title" id="featured-title">Selected work</h2>
        <a class="btn" href="portfolio/index.html">See all the work</a>
      </div>
      <ul class="work-grid">
        <li><a class="work-card" href="portfolio/index.html#fieldline">
          <img src="images/home/fieldline.webp" srcset="images/home/fieldline@2x.webp 2x" width="480" height="300" loading="lazy" alt="Fieldline website concept home page.">
          <span class="work-title">Fieldline website concept</span><span class="work-where">Web design</span>
        </a></li>
        <li><a class="work-card" href="portfolio/index.html#range-summary">
          <img src="images/home/range.webp" srcset="images/home/range@2x.webp 2x" width="480" height="300" loading="lazy" alt="Range Summary window comparing three date ranges.">
          <span class="work-title">Range Summary window</span><span class="work-where">Salient</span>
        </a></li>
        <li><a class="work-card" href="portfolio/index.html#social">
          <img src="images/home/social.webp" srcset="images/home/social@2x.webp 2x" width="480" height="300" loading="lazy" alt="Elmira College YouTube, Facebook and Instagram pages.">
          <span class="work-title">Social media from zero</span><span class="work-where">Elmira College</span>
        </a></li>
        <li><a class="work-card" href="portfolio/index.html#design-system">
          <img src="images/home/patterns.webp" srcset="images/home/patterns@2x.webp 2x" width="480" height="300" loading="lazy" alt="Pattern guide color page.">
          <span class="work-title">Design system</span><span class="work-where">Salient</span>
        </a></li>
      </ul>
    </section>

    <section class="wrap home-doors" aria-label="More">
      <ul class="doors">
        <li><a href="tools/index.html"><span class="door-name">Tools</span><span class="door-desc">Free tools for artists and designers: Creative Spark, the Image Grid Tool and the Color Palette Maker.</span></a></li>
        <li><a href="resume/index.html"><span class="door-name">Resume</span><span class="door-desc">Experience, education and skills, with a PDF to download.</span></a></li>
      </ul>
    </section>

    <section class="wrap about" id="about" aria-labelledby="about-title">
      <div class="about-side">
        <h2 class="section-title" id="about-title">About</h2>
        <img class="headshot" src="images/me/dan.webp" srcset="images/me/dan@2x.webp 2x" width="400" height="400" loading="lazy" alt="Dan Baroody">
      </div>
      <div>
        <p>I live and work in Elmira, New York. Every job starts the same way: I listen until I understand the problem, then I make what solves it. Over the years that has been dashboards for analysts, a website for prospective students, ads on a newspaper deadline, and small tools of my own.</p>
        <p>I work in Figma and Adobe Creative Cloud, write HTML and CSS, and build my own tools when the right one doesn't exist.</p>
      </div>
    </section>

    <section class="wrap cta" aria-labelledby="cta-title">
      <h2 id="cta-title">Hiring? Let's talk.</h2>
      <p>I'm looking for my next role. The fastest way to reach me is email.</p>
      <ul class="links">
        <li><a class="btn btn-primary" href="mailto:{EMAIL}">Email me</a></li>
        <li><a class="btn" href="resume/index.html">Read my resume</a></li>
        <li><a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn <svg class="btn-ico" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M6 3H3v10h10v-3M9 3h4v4M13 3L7 9" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="visually-hidden"> (opens in a new tab)</span></a></li>
      </ul>
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
log = log.replace('href="mockups/', 'href="../mockups/')
log = log.replace('<h2 class="section-title" id="solutions-title">Solutions</h2>\n        <p>', '<h2 class="section-title" id="solutions-title">Solutions</h2>\n        <p>')
import re as _re
log = _re.sub(r'\s*<div class="solutions-head">.*?</div>', '', log, flags=_re.S)
log = log.replace('aria-labelledby="solutions-title"', 'aria-label="Problems and solutions"')
portfolio = f"""    <section class="wrap page-head">
      <h1>Portfolio</h1>
      <p>Twelve years owning the product design of an enterprise analytics platform across web, mobile and desktop, plus the work that came before. Each line is a problem someone had. Open it to see what I made.</p>
      <p class="note">Client names and figures in the Salient screens are placeholders.</p>
      <div class="sort" role="group" aria-label="Organize the work">
        <span class="sort-label">Organize by</span>
        <button type="button" data-sort="project" aria-pressed="true">Project</button>
        <button type="button" data-sort="client" aria-pressed="false">Client</button>
        <button type="button" data-sort="type" aria-pressed="false">Type of solution</button>
      </div>
    </section>

{log}

{(ROOT / "modals.src.html").read_text()}"""
page("portfolio", "Portfolio, Dan Baroody",
     "Problems people had, and what Dan Baroody made to solve each one.",
     portfolio, current="Portfolio")

# ---------- Tools ----------
def tool(name, href, img, w, h, alt, desc, cls="shot"):
    return f"""      <article class="project">
        <div class="project-text">
          <h2 class="tool-name"><a href="../{href}">{name}</a></h2>
          <p>{desc}</p>
          <ul class="links"><li><a class="btn btn-primary" href="../{href}">Open {name}</a></li></ul>
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
{tool("Creative Spark", "Prompt-maker/creative-spark.html", "creative-spark-card", 1440, 900, "",
      "Sometimes creativity needs a spark. Two random words, and a refresh button (or the spacebar) for more. Use them to start a story, a sketch, a poem or a conversation.")}
{tool("Image Grid Tool", "Image-grid/image-grid.html", "image-grid-card", 1440, 900, "",
      "Upload an image, set the canvas size in inches and DPI, position the image, then lay a grid over it with your own rows, columns, line color and weight. Save the result and print it.")}
{tool("Color Palette Maker", "Color-palette/palette-maker.html", "palette-maker-card", 1440, 900, "",
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
    job("Lead UX &amp; UI Product Designer", "Salient, Big Flats, New York", "Jul 2014 – Present", [
        "Own end-to-end product design for Salient's enterprise analytics platform across web, mobile and desktop, leading major applications from concept and research through implementation, release and iteration.",
        'Set the design direction and product-wide standards: information architecture, interaction models, end-to-end user flows and visual standards shared by every client-facing application.',
        'Solve ambiguous, complex problems in data-heavy workflows through systems thinking, rapid prototyping and iterative testing, turning user research, customer feedback and business goals into clear design recommendations.',
        'Represent customer needs in product discussions with product, business and development teams, and build alignment across teams and stakeholders on what to build and why.',
        'Partner with engineers through implementation, guiding builds and resolving design questions until features ship the way they were designed.',
        'Built and continue to scale the product design system: reusable patterns, components and a documented pattern guide that keep new screens consistent and accessible across platforms.',
        'Design for accessibility and inclusion, including full keyboard support, screen reader labels, high-contrast states, reduced-motion support and larger touch targets.',
        'Apply user-centered methods throughout: usability evaluation, user testing and research synthesis, with findings fed back into product decisions.',
        'Wireframe and prototype in Balsamiq, Figma and working HTML and CSS, and use AI tools and LLMs to speed up exploration and prototyping.',
        'Contribute to the marketing team on web content, digital advertising and email campaigns, and advise the development team on email template structure.',
    ]),
    job("Director of Digital Content and Design", "Elmira College, Elmira, New York", "Feb 2008 – Jul 2014", [
        "Led the full redesign and launch of the college website, restructuring the information architecture around visitor goals so prospective students and families reached what they needed in fewer clicks, with the institution's priorities more visible.",
        'Interviewed prospective students one on one and synthesized what drove their decisions into recruitment content and site priorities.',
        'Managed and mentored a multidisciplinary team of creative and technical staff, providing direction, feedback and day-to-day guidance.',
        "Originated every one of the college's social media channels and developed new messaging that grew reach with the community, lapsed alumni and new students, increasing donations and engagement across every audience.",
        'Built the email marketing templates and oversaw campaigns running from student recruitment through alumni donations.',
        'Wrote, edited and designed print and digital publications, including viewbooks, brochures, newsletters and event materials.',
        'Worked directly with executives at every level to align messaging across departments, and prepared press releases, public statements and crisis communications.',
    ]),
    job("Creative Director", "inCommand Technologies, Corning, New York", "Aug 2006 – Mar 2008", [
        'Designed and built client websites end to end using a proprietary CMS, HTML and CSS, managing delivery for multiple clients at once.',
        'Created email marketing templates, campaign content and digital advertising for clients including Pyrex and World Kitchen.',
    ]),
    job("Graphic Designer", "Elmira Star-Gazette, Elmira, New York", "Sep 2005 – Aug 2006", [
        'Designed and produced print advertising in a high-volume, deadline-driven newsroom, managing 75+ ads and supporting assets each daily production cycle.',
        "Led the department's transition from film-based to fully digital production.",
    ]),
])

def skills(head, items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"<h3>{head}</h3><ul>{lis}</ul>"

resume = f"""    <section class="wrap page-head">
      <h1>Dan Baroody</h1>
      <p class="resume-title">Lead UX &amp; UI Product Designer</p>
      <p class="print-contact">Elmira, New York &nbsp; {EMAIL} &nbsp; linkedin.com/in/danbaroody &nbsp; www.dodill.com</p>
      <ul class="resume-actions">
        <li><a class="btn btn-primary" href="Dan-Baroody-Resume.pdf" download>Download PDF</a></li>
        <li><a class="btn" href="mailto:{EMAIL}">Email</a></li>
        <li><a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
      </ul>
    </section>

    <section class="wrap resume">
      <p class="resume-summary">I solve problems. For twelve years I have owned end-to-end product design for an enterprise analytics platform across web, mobile and desktop, turning dense, complicated data into experiences that are intuitive, useful and accessible. I lead major applications from research and prototypes through implementation and release, partner closely with product, business and engineering teams, and built the design system and reusable patterns that keep everything consistent. Before that I spent six and a half years in higher education, leading and mentoring a team and redesigning a college website around what students and families needed to find.</p>
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
            {skills('Product Design', ['End-to-end product design', 'Interaction models', 'Information architecture', 'User flows', 'Systems thinking', 'Enterprise and data-heavy UI', 'Web, mobile and desktop'])}
            {skills('Design Systems', ['Reusable patterns', 'Component libraries', 'Pattern documentation'])}
            {skills('Accessibility', ['Keyboard and screen reader', 'Contrast and reduced motion', 'Inclusive design'])}
            {skills('Research', ['Usability evaluation', 'User testing', 'User interviews', 'Research synthesis'])}
            {skills('Prototyping', ['Wireframing', 'Figma', 'Balsamiq', 'HTML &amp; CSS prototypes', 'Adobe XD', 'Storybook'])}
            {skills('AI &amp; Tools', ['Claude &amp; ChatGPT', 'AI-assisted design', 'Adobe Creative Suite'])}
            {skills('Collaboration', ['Cross-functional partnership', 'Stakeholder alignment', 'Engineering handoff', 'Mentoring and feedback'])}
          </div>
        </aside>
      </div>
      <section class="selected-work" aria-labelledby="sw-title">
        <h2 id="sw-title">Selected work</h2>
        <p class="sw-note">Each one links to its case study, with screenshots and interactive prototypes.</p>
        <ol class="sw-list">
          <li><h3><a href="../portfolio/index.html#range-summary">Range Summary window</a> <span>Salient</span></h3>
            <p><strong>Problem:</strong> Comparing date ranges on a chart opened a separate window for every range.</p>
            <p><strong>Solution:</strong> One window that holds every range side by side, highlights each range on the chart and calculates the differences between them, with full keyboard and screen reader support.</p></li>
          <li><h3><a href="../portfolio/index.html#directory">Dashboard directory</a> <span>Salient</span></h3>
            <p><strong>Problem:</strong> Nobody could find a dashboard unless they knew who saved it and where.</p>
            <p><strong>Solution:</strong> A search-first directory with filters, Recent and Favorites, grid and list views and adjustable density, prototyped in clickable HTML for team feedback.</p></li>
          <li><h3><a href="../portfolio/index.html#configure">Configure dialog</a> <span>Salient</span></h3>
            <p><strong>Problem:</strong> Every setup dialog worked a little differently, so people had to relearn each one.</p>
            <p><strong>Solution:</strong> One dialog with a shared available-and-selected pattern for group by, measures, date ranges, filters and options.</p></li>
          <li><h3><a href="../portfolio/index.html#design-system">Design system and pattern guide</a> <span>Salient</span></h3>
            <p><strong>Problem:</strong> Developers were guessing at colors, spacing and button states.</p>
            <p><strong>Solution:</strong> Documented foundations and reusable components: color, type, buttons, dialogs, form inputs, data grids, shuttle menus and a single-weight icon set.</p></li>
          <li><h3><a href="../portfolio/index.html#elmira-website">College website redesign</a> <span>Elmira College</span></h3>
            <p><strong>Problem:</strong> Prospective students and families could not quickly find how to visit, apply or pay.</p>
            <p><strong>Solution:</strong> Navigation grouped by visitor goals, calls to action on every page, and the college's priorities surfaced on the home page.</p></li>
          <li><h3><a href="../portfolio/index.html#social">Social media from zero</a> <span>Elmira College</span></h3>
            <p><strong>Problem:</strong> The college had no presence on social media.</p>
            <p><strong>Solution:</strong> Launched every channel with new messaging that reached the community, lapsed alumni and new students, increasing donations and engagement.</p></li>
          <li><h3><a href="../portfolio/index.html#fieldline">Fieldline website concept</a> <span>Personal project</span></h3>
            <p><strong>Problem:</strong> One company website has to speak to six different industries.</p>
            <p><strong>Solution:</strong> A 15-page marketing site hand-built in HTML, CSS and JavaScript, with shared templates so every page stays consistent.</p></li>
          <li><h3><a href="../portfolio/index.html#creative-spark">dodill creative tools</a> <span>Personal project</span></h3>
            <p><strong>Problem:</strong> Artists need small, focused help without the tool doing the creative work.</p>
            <p><strong>Solution:</strong> Creative Spark, an Image Grid Tool and a Color Palette Maker, all running in the browser.</p></li>
        </ol>
      </section>
    </section>"""
page("resume", "Resume, Dan Baroody",
     "Resume of Dan Baroody, Lead UX and UI Product Designer: end-to-end product design across web, mobile and desktop, design systems, accessibility and research. Elmira, New York.",
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
