#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the cow-cat GitHub profile set: banner / 3D garden / divider."""

# ---------------------------------------------------------------- palette
VARS_SHARED_LIGHT = """
--bg:#F0EEE6; --ink:#1F1E1D; --muted:#7D7A6F;
--cat:#FFFFFF; --catsh:#E9E5DA; --patch:#2E2A26;
--pink:#E8938C; --blush:#F2B3A8;
--yarn:#E8837E; --yarnd:#C96058; --heart:#E06253; --spark:#E3A93C;
--grass1:#A4C88B; --grass2:#8CB271; --tuft:#79A15E;
--shadow:rgba(40,38,35,.18); --cell:#E4E1D4;
--g1:#9BE9A8; --g2:#40C463; --g3:#30A14E; --g4:#216E39;
--sky:#FFFFFF; --star:#D8D4C6;
"""
VARS_SHARED_DARK = """
--bg:#262624; --ink:#F0EEE6; --muted:#8F8D85;
--cat:#F2F0E9; --catsh:#DCD9CE; --patch:#26231F;
--pink:#E8938C; --blush:#E89A8B;
--yarn:#E8837E; --yarnd:#C96058; --heart:#E4685A; --spark:#E9B84C;
--grass1:#43603F; --grass2:#374F34; --tuft:#54774E;
--shadow:rgba(0,0,0,.4); --cell:#34332F;
--g1:#0E4429; --g2:#006D32; --g3:#26A641; --g4:#39D353;
--sky:#3A3937; --star:#8F8D85;
"""
VARS_FACES_LIGHT = """
--t1:#9BE9A8; --l1:#82C48D; --r1:#699E72;
--t2:#40C463; --l2:#36A553; --r2:#2C8543;
--t3:#30A14E; --l3:#288740; --r3:#206B33;
--t4:#216E39; --l4:#1C5D30; --r4:#164A26;
"""
VARS_FACES_DARK = """
--t1:#0E4429; --l1:#0B3721; --r1:#092C1B;
--t2:#006D32; --l2:#005C2A; --r2:#004A22;
--t3:#26A641; --l3:#208B37; --r3:#19702C;
--t4:#39D353; --l4:#30B246; --r4:#268F38;
"""

UTIL = """
.mono{font-family:ui-monospace,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace}
.oc{transform-box:fill-box;transform-origin:50% 50%}
.ob{transform-box:fill-box;transform-origin:50% 100%}
.tailo{transform-box:fill-box;transform-origin:92% 88%}
.pawo{transform-box:fill-box;transform-origin:50% 8%}
"""

REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}\n"

# ---------------------------------------------------------------- cat art
# side view, faces right, local units u=6, feet baseline y=66, body 0..96 x
CAT_ART = """<g>
  <g class="tail tailo"><rect x="0" y="26" width="6" height="22" fill="var(--patch)"/><rect x="-5" y="19" width="8" height="8" fill="var(--cat)"/></g>
  <g class="gB"><rect x="72" y="52" width="6" height="14" fill="var(--catsh)"/><rect x="12" y="52" width="6" height="14" fill="var(--catsh)"/></g>
  <g class="gA"><rect x="24" y="52" width="6" height="14" fill="var(--cat)"/><g class="paw pawo"><rect x="60" y="52" width="6" height="14" fill="var(--cat)"/></g></g>
  <path fill="var(--cat)" d="M60,0 H66 V6 H72 V12 H78 V6 H84 V0 H90 V12 H96 V36 H84 V54 H6 V30 H54 V12 H60 Z"/>
  <rect x="6" y="48" width="78" height="6" fill="var(--catsh)"/>
  <g fill="var(--patch)">
    <rect x="6" y="30" width="30" height="12"/><rect x="6" y="42" width="24" height="6"/><rect x="12" y="48" width="12" height="6"/>
    <rect x="48" y="36" width="12" height="12"/>
    <rect x="54" y="12" width="16" height="6"/>
  </g>
  <g class="earF ob" fill="var(--patch)"><rect x="84" y="0" width="6" height="6"/><rect x="78" y="6" width="12" height="6"/></g>
  <rect x="64" y="7" width="4" height="4" fill="var(--pink)"/>
  <rect x="54" y="30" width="24" height="5" fill="var(--g3)"/>
  <rect x="63" y="35" width="5" height="5" fill="var(--spark)"/>
  <g class="blinkg oc"><rect x="78" y="18" width="6" height="6" fill="var(--patch)"/><rect x="82" y="19" width="2" height="2" fill="var(--cat)"/></g>
  <rect x="91" y="25" width="5" height="4" fill="var(--pink)"/>
  <rect x="78" y="27" width="8" height="3" fill="var(--blush)" opacity=".85"/>
  <rect x="96" y="21" width="10" height="2" fill="var(--muted)" opacity=".75"/>
  <rect x="96" y="26" width="10" height="2" fill="var(--muted)" opacity=".75"/>
</g>"""

YARN_ART = """<path fill="var(--yarn)" d="M8,0 H20 V4 H24 V8 H28 V20 H24 V24 H20 V28 H8 V24 H4 V20 H0 V8 H4 V4 H8 Z"/>
<g fill="var(--yarnd)"><rect x="6" y="6" width="16" height="3"/><rect x="4" y="13" width="20" height="3"/><rect x="8" y="20" width="14" height="3"/><rect x="24" y="11" width="7" height="3"/></g>"""

HEART_PATH = '<path fill="var(--heart)" d="M4,0 H8 V4 H12 V0 H16 V4 H20 V8 H16 V12 H12 V16 H8 V12 H4 V8 H0 V4 H4 Z"/>'

FLOWER = """<rect x="6" y="12" width="4" height="__STEM__" fill="var(--tuft)"/>
<rect x="4" y="0" width="4" height="4" fill="var(--sky2)"/><rect x="0" y="4" width="4" height="4" fill="var(--sky2)"/><rect x="8" y="4" width="4" height="4" fill="var(--sky2)"/><rect x="4" y="8" width="4" height="4" fill="var(--sky2)"/>
<rect x="4" y="4" width="4" height="4" fill="var(--spark)"/>""".replace('var(--sky2)', 'var(--cat)')

# ----------------------------------------------------------- real GH activity
LEVELMAP = {'NONE': 0, 'FIRST_QUARTILE': 1, 'SECOND_QUARTILE': 2, 'THIRD_QUARTILE': 3, 'FOURTH_QUARTILE': 4}

def _load_weeks():
    import subprocess, json
    q = 'query{viewer{contributionsCollection{contributionCalendar{weeks{contributionDays{contributionCount contributionLevel}}}}}}'
    out = subprocess.run(['gh', 'api', 'graphql', '-f', f'query={q}'], capture_output=True, text=True)
    if out.returncode != 0:
        print('warn: could not fetch contributions, using empty grid:', out.stderr.strip())
        return []
    data = json.loads(out.stdout)
    return data['data']['viewer']['contributionsCollection']['contributionCalendar']['weeks']

WEEKS = _load_weeks()

def banner_grid_from_weeks(cols=16, rows=4, day_idx=(0, 2, 4, 6)):
    wk = WEEKS[-cols:] if WEEKS else []
    filled, twinkle, pops = {}, {}, {}
    tw_classes = ['gtw1', 'gtw2', 'gtw3']
    cp_classes = ['cp1', 'cp2', 'cp3', 'cp4']
    cells = []  # (level, c, r)
    for c, week in enumerate(wk):
        days = week['contributionDays']
        for r, di in enumerate(day_idx[:rows]):
            if di >= len(days):
                continue
            lvl = LEVELMAP.get(days[di]['contributionLevel'], 0)
            if lvl > 0:
                filled[(c, r)] = f'g{lvl}'
                cells.append((lvl, c, r))
    cells.sort(reverse=True)
    for i, (lvl, c, r) in enumerate(cells[:3]):
        twinkle[(c, r)] = tw_classes[i % len(tw_classes)]
    for i, (lvl, c, r) in enumerate(cells[3:7]):
        pops[(c, r)] = (f'g{lvl}', cp_classes[i % len(cp_classes)])
    return filled, twinkle, pops

def garden_heights_from_weeks(cols=14, rows=6):
    wk = WEEKS[-cols:] if WEEKS else []
    H = [[0] * cols for _ in range(rows)]
    best = (0, -1, -1)
    for c, week in enumerate(wk):
        days = week['contributionDays']
        for r in range(rows):
            if r >= len(days):
                continue
            cnt = days[r]['contributionCount']
            lvl = LEVELMAP.get(days[r]['contributionLevel'], 0)
            H[r][c] = lvl
            if cnt > best[0]:
                best = (cnt, r, c)
    if best[0] > 0:
        H[best[1]][best[2]] = min(6, H[best[1]][best[2]] + 2)
    return H

# ================================================================= BANNER
def build_banner():
    css = """
:root{""" + VARS_SHARED_LIGHT + """}
.night{display:none}
@media (prefers-color-scheme:dark){
:root{""" + VARS_SHARED_DARK + """}
.day{display:none}
.night{display:inline}
}
""" + UTIL + """
/* yarn */
.yx{animation:yarnX 9s linear infinite}
.yy{animation:yarnY 9s linear infinite}
.yr{animation:yarnR 9s steps(1,end) infinite}
.ysh{animation:yarnSh 9s linear infinite}
.trail{animation:trailK 9s linear infinite}
@keyframes yarnX{0%,9%{transform:translateX(0)}12%{transform:translateX(110px)}15%{transform:translateX(195px)}18%{transform:translateX(255px)}20%{transform:translateX(285px)}23%{transform:translateX(315px)}26%{transform:translateX(335px)}29%{transform:translateX(350px)}31%{transform:translateX(355px)}34%{transform:translateX(370px)}37%{transform:translateX(383px)}40%{transform:translateX(395px)}43%,51%{transform:translateX(405px)}54%{transform:translateX(295px)}57%{transform:translateX(210px)}60%{transform:translateX(150px)}62%{transform:translateX(120px)}65%{transform:translateX(90px)}68%{transform:translateX(70px)}71%{transform:translateX(55px)}73%{transform:translateX(50px)}75%{transform:translateX(37px)}77%{transform:translateX(25px)}79%{transform:translateX(12px)}81%,100%{transform:translateX(0)}}
@keyframes yarnY{0%,9%{transform:translateY(0)}12%{transform:translateY(-52px)}15%{transform:translateY(-86px)}18%{transform:translateY(-106px)}20%{transform:translateY(-110px)}23%{transform:translateY(-102px)}26%{transform:translateY(-77px)}29%{transform:translateY(-36px)}31%{transform:translateY(0)}34%{transform:translateY(-22px)}37%{transform:translateY(-30px)}40%{transform:translateY(-22px)}43%,51%{transform:translateY(0)}54%{transform:translateY(-52px)}57%{transform:translateY(-86px)}60%{transform:translateY(-106px)}62%{transform:translateY(-110px)}65%{transform:translateY(-102px)}68%{transform:translateY(-77px)}71%{transform:translateY(-36px)}73%{transform:translateY(0)}75%{transform:translateY(-15px)}77%{transform:translateY(-22px)}79%{transform:translateY(-15px)}81%,100%{transform:translateY(0)}}
@keyframes yarnR{0%,9%{transform:rotate(0deg)}11%{transform:rotate(90deg)}13%{transform:rotate(180deg)}15%{transform:rotate(270deg)}17%{transform:rotate(360deg)}19%{transform:rotate(450deg)}21%{transform:rotate(540deg)}24%{transform:rotate(630deg)}27%{transform:rotate(720deg)}31%{transform:rotate(810deg)}35%{transform:rotate(900deg)}39%{transform:rotate(990deg)}43%,51%{transform:rotate(1080deg)}53%{transform:rotate(990deg)}55%{transform:rotate(900deg)}57%{transform:rotate(810deg)}59%{transform:rotate(720deg)}61%{transform:rotate(630deg)}63%{transform:rotate(540deg)}65%{transform:rotate(450deg)}67%{transform:rotate(360deg)}69%{transform:rotate(270deg)}71%{transform:rotate(180deg)}73%{transform:rotate(90deg)}77%,100%{transform:rotate(0deg)}}
@keyframes yarnSh{0%,9%{transform:translateX(0) scale(1)}12%{transform:translateX(110px) scale(.72)}15%{transform:translateX(195px) scale(.6)}18%{transform:translateX(255px) scale(.52)}20%{transform:translateX(285px) scale(.5)}23%{transform:translateX(315px) scale(.55)}26%{transform:translateX(335px) scale(.66)}29%{transform:translateX(350px) scale(.85)}31%{transform:translateX(355px) scale(1)}34%{transform:translateX(370px) scale(.9)}37%{transform:translateX(383px) scale(.85)}40%{transform:translateX(395px) scale(.9)}43%,51%{transform:translateX(405px) scale(1)}54%{transform:translateX(295px) scale(.62)}57%{transform:translateX(210px) scale(.52)}60%{transform:translateX(150px) scale(.5)}62%{transform:translateX(120px) scale(.5)}65%{transform:translateX(90px) scale(.6)}68%{transform:translateX(70px) scale(.72)}71%{transform:translateX(55px) scale(.88)}73%{transform:translateX(50px) scale(1)}75%{transform:translateX(37px) scale(.94)}77%{transform:translateX(25px) scale(.88)}79%{transform:translateX(12px) scale(.94)}81%,100%{transform:translateX(0) scale(1)}}
@keyframes trailK{0%,9%{stroke-dashoffset:405}12%{stroke-dashoffset:295}15%{stroke-dashoffset:210}18%{stroke-dashoffset:150}20%{stroke-dashoffset:120}23%{stroke-dashoffset:90}26%{stroke-dashoffset:70}29%{stroke-dashoffset:55}31%{stroke-dashoffset:50}34%{stroke-dashoffset:35}37%{stroke-dashoffset:22}40%{stroke-dashoffset:10}43%,51%{stroke-dashoffset:0}54%{stroke-dashoffset:110}57%{stroke-dashoffset:195}60%{stroke-dashoffset:255}62%{stroke-dashoffset:285}65%{stroke-dashoffset:315}68%{stroke-dashoffset:335}71%{stroke-dashoffset:350}73%{stroke-dashoffset:355}75%{stroke-dashoffset:368}77%{stroke-dashoffset:380}79%{stroke-dashoffset:393}81%,100%{stroke-dashoffset:405}}
/* cat */
.cx{animation:catX 9s linear infinite}
.cb{animation:catBob 9s linear infinite}
.cf{animation:catFace 9s steps(1,end) infinite}
.ct{animation:catTilt 9s linear infinite}
.cs{animation:catSq 9s linear infinite}
.tail{animation:tailSw 2.4s ease-in-out infinite alternate}
.earF{animation:earFk 4.7s linear infinite}
.blinkg{animation:blinkK 4.6s linear infinite}
.gA{animation:gaitA 9s steps(1,end) infinite}
.gB{animation:gaitB 9s steps(1,end) infinite}
.paw{animation:pawK 9s linear infinite}
@keyframes catX{0%,20%{transform:translateX(0)}24%{transform:translateX(62px)}28%{transform:translateX(154px)}32%{transform:translateX(256px)}36%{transform:translateX(358px)}40%{transform:translateX(450px)}44%{transform:translateX(520px)}48%,54%{transform:translateX(555px)}58%{transform:translateX(483px)}62%{transform:translateX(392px)}66%{transform:translateX(300px)}70%{transform:translateX(206px)}74%{transform:translateX(123px)}78%{transform:translateX(60px)}82%{transform:translateX(19px)}86%,100%{transform:translateX(0)}}
@keyframes catBob{0%{transform:translateY(0)}3%{transform:translateY(-2px)}6%,9%{transform:translateY(0)}10.5%{transform:translateY(-10px)}13%,20%{transform:translateY(0)}22%{transform:translateY(-5px)}24%{transform:translateY(0)}26%{transform:translateY(-5px)}28%{transform:translateY(0)}30%{transform:translateY(-5px)}32%{transform:translateY(0)}34%{transform:translateY(-5px)}36%{transform:translateY(0)}38%{transform:translateY(-5px)}40%{transform:translateY(0)}42%{transform:translateY(-5px)}44%{transform:translateY(0)}46%{transform:translateY(-5px)}48%,50%{transform:translateY(0)}52%{transform:translateY(-9px)}54%,56%{transform:translateY(0)}58%{transform:translateY(-4px)}60%{transform:translateY(0)}62%{transform:translateY(-4px)}64%{transform:translateY(0)}66%{transform:translateY(-4px)}68%{transform:translateY(0)}70%{transform:translateY(-4px)}72%{transform:translateY(0)}74%{transform:translateY(-4px)}76%{transform:translateY(0)}78%{transform:translateY(-4px)}80%{transform:translateY(0)}82%{transform:translateY(-4px)}84%,88%{transform:translateY(0)}89.5%{transform:translateY(-14px)}91%{transform:translateY(0)}93%{transform:translateY(-9px)}95%,100%{transform:translateY(0)}}
@keyframes catFace{0%,48%{transform:scaleX(1)}48.5%,87%{transform:scaleX(-1)}88%,100%{transform:scaleX(1)}}
@keyframes catTilt{0%,4%{transform:rotate(0deg)}6%,9%{transform:rotate(-7deg)}10%{transform:rotate(9deg)}13%{transform:rotate(2deg)}16%{transform:rotate(0deg)}22%,46%{transform:rotate(6deg)}48%{transform:rotate(0deg)}49%,51%{transform:rotate(7deg)}52%{transform:rotate(-9deg)}54%{transform:rotate(-2deg)}57%,84%{transform:rotate(-6deg)}87%,100%{transform:rotate(0deg)}}
@keyframes catSq{0%,8%{transform:scale(1,1)}9%{transform:scale(1.1,.88)}10.5%{transform:scale(.94,1.08)}13%{transform:scale(1.04,.96)}15%,48%{transform:scale(1,1)}50%{transform:scale(1.08,.9)}52%{transform:scale(.94,1.07)}54%{transform:scale(1.03,.97)}56%,88%{transform:scale(1,1)}88.5%{transform:scale(1.08,.9)}89.5%{transform:scale(.95,1.06)}91%{transform:scale(1.04,.95)}92.5%{transform:scale(1,1)}93.5%{transform:scale(.96,1.05)}95%{transform:scale(1.03,.97)}96.5%,100%{transform:scale(1,1)}}
@keyframes tailSw{from{transform:rotate(-8deg)}to{transform:rotate(10deg)}}
@keyframes earFk{0%,88%{transform:rotate(0deg)}91%{transform:rotate(14deg)}93%,100%{transform:rotate(0deg)}}
@keyframes blinkK{0%,91%{transform:scaleY(1)}93%,95%{transform:scaleY(.12)}97%,100%{transform:scaleY(1)}}
@keyframes gaitA{0%,20%{transform:translateY(0)}21%{transform:translateY(-3px)}23%{transform:translateY(0)}25%{transform:translateY(-3px)}27%{transform:translateY(0)}29%{transform:translateY(-3px)}31%{transform:translateY(0)}33%{transform:translateY(-3px)}35%{transform:translateY(0)}37%{transform:translateY(-3px)}39%{transform:translateY(0)}41%{transform:translateY(-3px)}43%{transform:translateY(0)}45%{transform:translateY(-3px)}47%,56%{transform:translateY(0)}57%{transform:translateY(-3px)}59%{transform:translateY(0)}61%{transform:translateY(-3px)}63%{transform:translateY(0)}65%{transform:translateY(-3px)}67%{transform:translateY(0)}69%{transform:translateY(-3px)}71%{transform:translateY(0)}73%{transform:translateY(-3px)}75%{transform:translateY(0)}77%{transform:translateY(-3px)}79%{transform:translateY(0)}81%{transform:translateY(-3px)}83%{transform:translateY(0)}85%{transform:translateY(-3px)}86%,100%{transform:translateY(0)}}
@keyframes gaitB{0%,22%{transform:translateY(0)}23%{transform:translateY(-3px)}25%{transform:translateY(0)}27%{transform:translateY(-3px)}29%{transform:translateY(0)}31%{transform:translateY(-3px)}33%{transform:translateY(0)}35%{transform:translateY(-3px)}37%{transform:translateY(0)}39%{transform:translateY(-3px)}41%{transform:translateY(0)}43%{transform:translateY(-3px)}45%{transform:translateY(0)}47%{transform:translateY(-3px)}48%,58%{transform:translateY(0)}59%{transform:translateY(-3px)}61%{transform:translateY(0)}63%{transform:translateY(-3px)}65%{transform:translateY(0)}67%{transform:translateY(-3px)}69%{transform:translateY(0)}71%{transform:translateY(-3px)}73%{transform:translateY(0)}75%{transform:translateY(-3px)}77%{transform:translateY(0)}79%{transform:translateY(-3px)}81%{transform:translateY(0)}83%{transform:translateY(-3px)}85%,100%{transform:translateY(0)}}
@keyframes pawK{0%,8.5%{transform:rotate(0deg)}9.5%{transform:rotate(-46deg)}11.5%,49.8%{transform:rotate(0deg)}50.8%{transform:rotate(-46deg)}52.5%,100%{transform:rotate(0deg)}}
/* effects */
.puff1{animation:puff1 9s linear infinite}
.puff2{animation:puff2 9s linear infinite}
.puff3{animation:puff3 9s linear infinite}
.puff4{animation:puff4 9s linear infinite}
@keyframes puff1{0%,31%{opacity:0;transform:translateY(0) scale(.4)}33%{opacity:.7;transform:translateY(-3px) scale(.7)}40%,100%{opacity:0;transform:translateY(-10px) scale(1.3)}}
@keyframes puff2{0%,43.5%{opacity:0;transform:translateY(0) scale(.3)}45%{opacity:.55;transform:translateY(-2px) scale(.6)}50%,100%{opacity:0;transform:translateY(-8px) scale(1.1)}}
@keyframes puff3{0%,73.5%{opacity:0;transform:translateY(0) scale(.4)}75%{opacity:.7;transform:translateY(-3px) scale(.7)}81%,100%{opacity:0;transform:translateY(-10px) scale(1.25)}}
@keyframes puff4{0%,81.5%{opacity:0;transform:translateY(0) scale(.3)}83%{opacity:.5;transform:translateY(-2px) scale(.6)}88%,100%{opacity:0;transform:translateY(-7px) scale(1)}}
.spk1{animation:spark1 9s linear infinite}
.spk2{animation:spark2 9s linear infinite}
@keyframes spark1{0%,8.5%{opacity:0;transform:scale(.3) rotate(0deg)}10%{opacity:1;transform:scale(1) rotate(20deg)}14.5%,100%{opacity:0;transform:scale(1.2) rotate(45deg)}}
@keyframes spark2{0%,50.3%{opacity:0;transform:scale(.3) rotate(0deg)}51.8%{opacity:1;transform:scale(1) rotate(20deg)}56.5%,100%{opacity:0;transform:scale(1.2) rotate(45deg)}}
.heart1{animation:heart1 9s linear infinite}
.heart2{animation:heart2 9s linear infinite}
@keyframes heart1{0%,88%{opacity:0;transform:translateY(6px) scale(.4)}90%{opacity:1;transform:translateY(0) scale(1.08)}93%{opacity:1;transform:translateY(-8px) scale(1)}97%{opacity:.85;transform:translateY(-16px) scale(1)}100%{opacity:0;transform:translateY(-22px) scale(1)}}
@keyframes heart2{0%,90.5%{opacity:0;transform:translateY(6px) scale(.3)}92.5%{opacity:1;transform:translateY(0) scale(.85)}100%{opacity:0;transform:translateY(-18px) scale(.85)}}
/* sky */
.tw1{animation:tw 3.4s ease-in-out infinite}
.tw2{animation:tw 3.4s ease-in-out 1.2s infinite}
.tw3{animation:tw 3.4s ease-in-out 2.3s infinite}
@keyframes tw{0%,100%{opacity:.25}50%{opacity:1}}
.gtw1{animation:gtwK 3s ease-in-out infinite}
.gtw2{animation:gtwK 3s ease-in-out 1s infinite}
.gtw3{animation:gtwK 3s ease-in-out 2s infinite}
@keyframes gtwK{0%,100%{opacity:.55}50%{opacity:1}}
.cp1{animation:cp1 9s linear infinite}
.cp2{animation:cp2 9s linear infinite}
.cp3{animation:cp3 9s linear infinite}
.cp4{animation:cp4 9s linear infinite}
@keyframes cp1{0%,14%{opacity:0;transform:scale(.3)}15.5%{opacity:1;transform:scale(1.3)}17%,100%{opacity:1;transform:scale(1)}}
@keyframes cp2{0%,34%{opacity:0;transform:scale(.3)}35.5%{opacity:1;transform:scale(1.3)}37%,100%{opacity:1;transform:scale(1)}}
@keyframes cp3{0%,59%{opacity:0;transform:scale(.3)}60.5%{opacity:1;transform:scale(1.3)}62%,100%{opacity:1;transform:scale(1)}}
@keyframes cp4{0%,84%{opacity:0;transform:scale(.3)}85.5%{opacity:1;transform:scale(1.3)}87%,100%{opacity:1;transform:scale(1)}}
.dr1{animation:drift 8s ease-in-out infinite alternate}
.dr2{animation:drift 11s ease-in-out infinite alternate-reverse}
@keyframes drift{from{transform:translateX(0)}to{transform:translateX(16px)}}
.flower{animation:sway 3.6s ease-in-out infinite alternate}
.flower2{animation:sway 3.6s ease-in-out .8s infinite alternate}
@keyframes sway{from{transform:rotate(-3deg)}to{transform:rotate(3deg)}}
/* spinner + typing */
.sq{animation:sqp 1.6s ease-in-out infinite alternate}
@keyframes sqp{from{opacity:.5}to{opacity:1}}
.sp{font-size:13px;fill:var(--muted)}
.sp1{animation:sp1 9s steps(1,end) infinite}
.sp2{animation:sp2 9s steps(1,end) infinite}
.sp3{animation:sp3 9s steps(1,end) infinite}
@keyframes sp1{0%,32%{opacity:1}33%,100%{opacity:0}}
@keyframes sp2{0%,32%{opacity:0}33%,65%{opacity:1}66%,100%{opacity:0}}
@keyframes sp3{0%,65%{opacity:0}66%,100%{opacity:1}}
.ch1{animation:chK1 9s linear infinite}
.ch2{animation:chK2 9s linear infinite}
.ch3{animation:chK3 9s linear infinite}
.ch4{animation:chK4 9s linear infinite}
.ch5{animation:chK5 9s linear infinite}
.ch6{animation:chK6 9s linear infinite}
.ch7{animation:chK7 9s linear infinite}
.ch8{animation:chK8 9s linear infinite}
.ch9{animation:chK9 9s linear infinite}
@keyframes chK1{0%,6.7%{opacity:0}7%,100%{opacity:1}}
@keyframes chK2{0%,8.2%{opacity:0}8.5%,100%{opacity:1}}
@keyframes chK3{0%,9.8%{opacity:0}10.1%,100%{opacity:1}}
@keyframes chK4{0%,12.9%{opacity:0}13.2%,100%{opacity:1}}
@keyframes chK5{0%,14.4%{opacity:0}14.7%,100%{opacity:1}}
@keyframes chK6{0%,16%{opacity:0}16.3%,100%{opacity:1}}
@keyframes chK7{0%,19.1%{opacity:0}19.4%,100%{opacity:1}}
@keyframes chK8{0%,20.7%{opacity:0}21%,100%{opacity:1}}
@keyframes chK9{0%,22.2%{opacity:0}22.5%,100%{opacity:1}}
.cur{animation:curMove 9s steps(1,end) infinite,curBlink 1.06s steps(1,end) infinite}
@keyframes curMove{0%{transform:translateX(0)}6.7%{transform:translateX(24px)}8.2%{transform:translateX(48px)}9.8%{transform:translateX(60px)}11.3%{transform:translateX(72px)}12.9%{transform:translateX(96px)}14.4%{transform:translateX(108px)}16%{transform:translateX(144px)}17.6%{transform:translateX(156px)}19.1%{transform:translateX(180px)}20.7%{transform:translateX(204px)}22.2%,100%{transform:translateX(234px)}}
@keyframes curBlink{0%,50%{opacity:1}51%,100%{opacity:0}}
""" + REDUCED

    # ---- contribution grid (sky) ----
    gx, gy, pitch = 688, 34, 11
    filled, twinkle, pops = banner_grid_from_weeks(cols=14)
    grid = []
    for r in range(4):
        for c in range(16):
            x, y = gx + c*pitch, gy + r*pitch
            grid.append(f'<rect x="{x}" y="{y}" width="8" height="8" rx="2" fill="var(--cell)"/>')
    for (c,r),col in filled.items():
        x, y = gx + c*pitch, gy + r*pitch
        cls = f' class="{twinkle[(c,r)]}"' if (c,r) in twinkle else ''
        grid.append(f'<rect{cls} x="{x}" y="{y}" width="8" height="8" rx="2" fill="var(--{col})"/>')
    for (c,r),(col,cls) in pops.items():
        x, y = gx + c*pitch, gy + r*pitch
        grid.append(f'<rect class="{cls} oc" x="{x}" y="{y}" width="8" height="8" rx="2" fill="var(--{col})" opacity="0"/>')
    grid_svg = '\n  '.join(grid)

    body = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 300" width="900" height="300" role="img" aria-label="pixel cow-cat chasing yarn — HI, I'M YUN">
<title>HI, I'M YUN — cow-cat &amp; yarn</title>
<style>{css}</style>
<defs>
<clipPath id="frame"><rect x="0" y="0" width="900" height="300" rx="16"/></clipPath>
<g id="star4"><rect x="4.5" y="0" width="3" height="12"/><rect x="0" y="4.5" width="12" height="3"/></g>
<g id="sp4"><rect x="5" y="0" width="4" height="14"/><rect x="0" y="5" width="14" height="4"/></g>
<g id="sp3s"><rect x="3.5" y="0" width="3" height="10"/><rect x="0" y="3.5" width="10" height="3"/></g>
</defs>
<rect x="0" y="0" width="900" height="300" rx="16" fill="var(--bg)"/>
<g clip-path="url(#frame)">

<g class="night" fill="var(--star)">
  <use href="#star4" x="330" y="60" class="tw1"/>
  <use href="#star4" x="430" y="40" class="tw2"/>
  <use href="#star4" x="520" y="88" class="tw3"/>
  <use href="#star4" x="600" y="52" class="tw1"/>
  <use href="#star4" x="90" y="148" class="tw2"/>
  <rect x="250" y="56" width="3" height="3" class="tw3"/>
  <rect x="480" y="130" width="3" height="3" class="tw1"/>
  <rect x="370" y="110" width="3" height="3" class="tw2"/>
  <rect x="640" y="120" width="3" height="3" class="tw3"/>
</g>
<g class="day" fill="var(--sky)" opacity=".9">
  <g transform="translate(300,52)" class="dr1"><rect x="12" y="0" width="18" height="6.5"/><rect x="6" y="6" width="36" height="6.5"/><rect x="0" y="12" width="48" height="6"/></g>
  <g transform="translate(560,80)" class="dr2"><rect x="10" y="0" width="15" height="5.5"/><rect x="5" y="5" width="25" height="5.5"/><rect x="0" y="10" width="35" height="5"/></g>
</g>

<!-- contribution sky -->
<g>
  {grid_svg}
</g>

<!-- ground -->
<rect x="0" y="254" width="900" height="18.5" fill="var(--grass1)"/>
<rect x="0" y="272" width="900" height="28" fill="var(--grass2)"/>
<g fill="var(--grass1)">
  <rect x="24" y="272" width="8" height="6"/><rect x="120" y="272" width="8" height="6"/><rect x="216" y="272" width="8" height="6"/><rect x="318" y="272" width="8" height="6"/><rect x="414" y="272" width="8" height="6"/><rect x="516" y="272" width="8" height="6"/><rect x="612" y="272" width="8" height="6"/><rect x="708" y="272" width="8" height="6"/><rect x="804" y="272" width="8" height="6"/><rect x="876" y="272" width="8" height="6"/>
</g>
<g fill="var(--grass2)" opacity=".6">
  <rect x="250" y="262" width="8" height="4"/><rect x="430" y="266" width="8" height="4"/><rect x="560" y="260" width="8" height="4"/><rect x="676" y="264" width="8" height="4"/><rect x="820" y="262" width="8" height="4"/>
</g>
<g fill="var(--tuft)">
  <g transform="translate(70,242)"><rect x="0" y="0" width="4" height="12"/><rect x="7" y="4" width="4" height="8"/></g>
  <g transform="translate(340,244)"><rect x="0" y="0" width="4" height="10"/><rect x="6" y="3" width="4" height="7"/></g>
  <g transform="translate(470,242)"><rect x="0" y="0" width="4" height="12"/><rect x="7" y="5" width="4" height="7"/></g>
  <g transform="translate(600,244)"><rect x="0" y="0" width="4" height="10"/><rect x="6" y="2" width="4" height="8"/></g>
  <g transform="translate(724,242)"><rect x="0" y="0" width="4" height="12"/><rect x="7" y="4" width="4" height="8"/></g>
  <g transform="translate(856,244)"><rect x="0" y="0" width="4" height="10"/><rect x="6" y="3" width="4" height="7"/></g>
</g>
<g transform="translate(394,230)"><g class="flower ob">{FLOWER.replace('__STEM__','12')}</g></g>
<g transform="translate(742,226)"><g class="flower2 ob">{FLOWER.replace('__STEM__','16')}</g></g>
<g transform="translate(824,234)"><g class="flower ob">{FLOWER.replace('__STEM__','8')}</g></g>

<!-- shadows -->
<g transform="translate(153,256)"><g class="cx"><ellipse cx="0" cy="0" rx="38" ry="5" fill="var(--shadow)"/></g></g>
<g transform="translate(235,256)"><g class="ysh oc"><ellipse cx="0" cy="0" rx="15" ry="3.5" fill="var(--shadow)"/></g></g>

<!-- dust -->
<g transform="translate(584,246)"><g class="puff1 oc" opacity="0" fill="var(--muted)"><rect x="0" y="0" width="5" height="5"/><rect x="9" y="-5" width="4" height="4"/><rect x="7" y="5" width="4" height="4"/><rect x="-6" y="-2" width="3" height="3"/></g></g>
<g transform="translate(634,248)"><g class="puff2 oc" opacity="0" fill="var(--muted)"><rect x="0" y="0" width="4" height="4"/><rect x="7" y="-4" width="3" height="3"/><rect x="-5" y="-1" width="3" height="3"/></g></g>
<g transform="translate(279,246)"><g class="puff3 oc" opacity="0" fill="var(--muted)"><rect x="0" y="0" width="5" height="5"/><rect x="-9" y="-5" width="4" height="4"/><rect x="-7" y="5" width="4" height="4"/><rect x="6" y="-2" width="3" height="3"/></g></g>
<g transform="translate(229,248)"><g class="puff4 oc" opacity="0" fill="var(--muted)"><rect x="0" y="0" width="4" height="4"/><rect x="-7" y="-4" width="3" height="3"/><rect x="5" y="-1" width="3" height="3"/></g></g>

<!-- yarn thread + ball -->
<path class="trail" d="M235,251 H640" pathLength="405" stroke="var(--yarn)" stroke-width="2.5" fill="none" opacity=".8" stroke-dasharray="405" stroke-dashoffset="405"/>
<g transform="translate(221,226)"><g class="yx"><g class="yy"><g class="yr oc">
{YARN_ART}
</g></g></g></g>

<!-- cat -->
<g transform="translate(105,188)"><g class="cx"><g class="cb"><g class="cf oc"><g class="ct ob"><g class="cs ob">
{CAT_ART}
</g></g></g></g></g></g>

<!-- sparkles & hearts -->
<g transform="translate(208,196)"><g class="spk1 oc" opacity="0" fill="var(--spark)"><use href="#sp4" x="0" y="6"/><use href="#sp3s" x="26" y="-8"/><use href="#sp3s" x="-8" y="30"/></g></g>
<g transform="translate(630,194)"><g class="spk2 oc" opacity="0" fill="var(--spark)"><use href="#sp4" x="4" y="4"/><use href="#sp3s" x="30" y="-6"/><use href="#sp3s" x="-10" y="26"/></g></g>
<g transform="translate(170,148)"><g class="heart1 oc" opacity="0">{HEART_PATH}</g></g>
<g transform="translate(200,160)"><g class="heart2 oc" opacity="0">{HEART_PATH}</g></g>

<!-- spinner -->
<g transform="translate(28,22)">
  <rect class="sq" x="0" y="1" width="10" height="10" rx="2" fill="var(--g3)"/>
  <text class="mono sp sp1" x="20" y="11" opacity="1">$ git checkout -b play/yarn</text>
  <text class="mono sp sp2" x="20" y="11" opacity="0">$ git push cat --force</text>
  <text class="mono sp sp3" x="20" y="11" opacity="0">$ git commit -m 'purrfect'</text>
</g>

<!-- HI, I'M YUN -->
<g transform="translate(30,84)">
  <g class="ch1" fill="var(--ink)"><rect x="0" y="0" width="6" height="30"/><rect x="12" y="0" width="6" height="30"/><rect x="5.5" y="12" width="7" height="6"/></g>
  <g class="ch2" fill="var(--ink)" transform="translate(24,0)"><rect x="0" y="0" width="18" height="6"/><rect x="6" y="5.5" width="6" height="19"/><rect x="0" y="24" width="18" height="6"/></g>
  <g class="ch3" fill="var(--ink)" transform="translate(48,0)"><rect x="0" y="24" width="6" height="12"/></g>
  <g class="ch4" fill="var(--ink)" transform="translate(72,0)"><rect x="0" y="0" width="18" height="6"/><rect x="6" y="5.5" width="6" height="19"/><rect x="0" y="24" width="18" height="6"/></g>
  <g class="ch5" fill="var(--ink)" transform="translate(96,0)"><rect x="0" y="0" width="6" height="12"/></g>
  <g class="ch6" fill="var(--ink)" transform="translate(108,0)"><rect x="0" y="0" width="6" height="30"/><rect x="24" y="0" width="6" height="30"/><rect x="6" y="6" width="6" height="6"/><rect x="18" y="6" width="6" height="6"/><rect x="12" y="12" width="6" height="6"/></g>
  <g class="ch7" fill="var(--g3)" transform="translate(156,0)"><rect x="0" y="0" width="6" height="12"/><rect x="12" y="0" width="6" height="12"/><rect x="6" y="11.5" width="6" height="18.5"/></g>
  <g class="ch8" fill="var(--g3)" transform="translate(180,0)"><rect x="0" y="0" width="6" height="24.5"/><rect x="12" y="0" width="6" height="24.5"/><rect x="0" y="24" width="18" height="6"/></g>
  <g class="ch9" fill="var(--g3)" transform="translate(204,0)"><rect x="0" y="0" width="6" height="30"/><rect x="18" y="0" width="6" height="30"/><rect x="6" y="6" width="6" height="6"/><rect x="12" y="12" width="6" height="6"/></g>
  <rect class="cur" x="0" y="0" width="12" height="30" fill="var(--g3)" transform="translate(234,0)"/>
</g>

<!-- signature -->
<text class="mono" x="866" y="290" font-size="10" letter-spacing="2" text-anchor="end" fill="var(--muted)" opacity=".75">yunc-star</text>
<g fill="var(--spark)"><rect x="872" y="281" width="2" height="6"/><rect x="870" y="283" width="6" height="2"/></g>

</g>
</svg>"""
    return body

# ================================================================= GARDEN
def build_garden():
    a, z = 16, 11
    X0, Y0 = 386, 64
    H = garden_heights_from_weeks()
    def lvl(h):
        return 1 if h == 1 else 2 if h == 2 else 3 if h == 3 else 4

    items = []
    for r in range(6):
        for c in range(14):
            items.append((r + c, r, c))
    items.sort()
    floor = []
    tiles = []
    shimmer_targets = {(2,10),(2,11),(1,12)}
    for _, r, c in items:
        h = H[r][c]
        cx = X0 + (c - r) * a
        cy = Y0 + (c + r) * a // 2
        delay = 0.15 + (r + c) * 0.055
        op = '.95' if (r + c) % 2 == 0 else '.7'
        floor.append(
            f'<g class="gwf" style="animation-delay:{delay:.2f}s">'
            f'<path d="M{cx},{cy-8} L{cx+16},{cy} L{cx},{cy+8} L{cx-16},{cy} Z" fill="var(--cell)" opacity="{op}"/></g>')
        if h > 0:
            L = lvl(h); hz = h * z; ty = cy - hz
            shim = ' class="shim"' if (r, c) in shimmer_targets else ''
            tiles.append(
                f'<g class="gw ob" style="animation-delay:{delay + 0.25:.2f}s">'
                f'<path d="M{cx-16},{ty} L{cx},{ty+8} L{cx},{cy+8} L{cx-16},{cy} Z" fill="var(--l{L})"/>'
                f'<path d="M{cx+16},{ty} L{cx},{ty+8} L{cx},{cy+8} L{cx+16},{cy} Z" fill="var(--r{L})"/>'
                f'<path{shim} d="M{cx},{ty-8} L{cx+16},{ty} L{cx},{ty+8} L{cx-16},{ty} Z" fill="var(--t{L})"/>'
                f'</g>')
    tiles_svg = '\n  '.join(floor) + '\n  ' + '\n  '.join(tiles)

    css = """
:root{""" + VARS_SHARED_LIGHT + VARS_FACES_LIGHT + """}
@media (prefers-color-scheme:dark){
:root{""" + VARS_SHARED_DARK + VARS_FACES_DARK + """}
}
""" + UTIL + """
.gw{animation:grow .55s cubic-bezier(.34,1.4,.5,1) both}
@keyframes grow{from{transform:scaleY(0)}to{transform:scaleY(1)}}
.gwf{animation:fadeT .5s ease-out both}
@keyframes fadeT{from{opacity:0}to{opacity:1}}
.fin{animation:finK .6s ease-out both}
@keyframes finK{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.shim{animation:shimK 3.2s ease-in-out infinite}
@keyframes shimK{0%,100%{opacity:1}50%{opacity:.75}}
.tail{animation:tailSw 2.4s ease-in-out infinite alternate}
@keyframes tailSw{from{transform:rotate(-8deg)}to{transform:rotate(10deg)}}
.blinkg{animation:blinkK 4.6s linear infinite}
@keyframes blinkK{0%,91%{transform:scaleY(1)}93%,95%{transform:scaleY(.12)}97%,100%{transform:scaleY(1)}}
.hg{animation:hgK 7s linear infinite}
@keyframes hgK{0%,74%{opacity:0;transform:translateY(4px) scale(.4)}78%{opacity:1;transform:translateY(0) scale(1)}90%{opacity:.9;transform:translateY(-12px) scale(1)}100%{opacity:0;transform:translateY(-18px) scale(1)}}
.tw1{animation:tw 3.4s ease-in-out infinite}
.tw2{animation:tw 3.4s ease-in-out 1.6s infinite}
@keyframes tw{0%,100%{opacity:.25}50%{opacity:1}}
""" + REDUCED

    body = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 300" width="900" height="300" role="img" aria-label="isometric contribution garden with a cow-cat on top">
<title>contribution garden — yunc-star</title>
<style>{css}</style>
<defs>
<clipPath id="frame"><rect x="0" y="0" width="900" height="300" rx="16"/></clipPath>
<g id="sp4"><rect x="5" y="0" width="4" height="14"/><rect x="0" y="5" width="14" height="4"/></g>
</defs>
<rect x="0" y="0" width="900" height="300" rx="16" fill="var(--bg)"/>
<g clip-path="url(#frame)">

  <ellipse cx="470" cy="222" rx="175" ry="10" fill="var(--shadow)" opacity=".3"/>
  {tiles_svg}

  <g fill="var(--spark)">
    <use href="#sp4" x="656" y="60" class="tw1"/>
    <use href="#sp4" x="300" y="152" class="tw2"/>
  </g>

  <g class="fin" style="animation-delay:1.55s">
    <g transform="translate(488,121) scale(.75)"><g class="oc">{YARN_ART}</g></g>
  </g>
  <g class="fin" style="animation-delay:1.4s">
    <g transform="translate(482,45) scale(.8333)">{CAT_ART}</g>
  </g>
  <g transform="translate(540,22)"><g class="hg oc" opacity="0">{HEART_PATH}</g></g>

  <g class="fin" style="animation-delay:1.9s">
    <text class="mono" x="28" y="282" font-size="12" fill="var(--muted)">@yunc-star</text>
    <text class="mono" x="872" y="282" font-size="12" text-anchor="end" fill="var(--muted)">contribution garden</text>
  </g>

</g>
</svg>"""
    return body

# ================================================================= DIVIDER
def build_divider():
    css = """
:root{""" + VARS_SHARED_LIGHT + """}
@media (prefers-color-scheme:dark){
:root{""" + VARS_SHARED_DARK + """}
}
""" + UTIL + """
.catW{animation:walkC 16s linear infinite}
@keyframes walkC{from{transform:translateX(-190px)}to{transform:translateX(1040px)}}
.rollW{animation:rollK .9s steps(8,end) infinite}
@keyframes rollK{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
.bobW{animation:bobK .28s steps(1,end) infinite}
@keyframes bobK{0%,49.9%{transform:translateY(0)}50%,100%{transform:translateY(-2px)}}
.gA{animation:gK .28s steps(1,end) infinite}
.gB{animation:gK .28s steps(1,end) .14s infinite}
@keyframes gK{0%,49.9%{transform:translateY(0)}50%,100%{transform:translateY(-3px)}}
.tail{animation:tailSw 1.6s ease-in-out infinite alternate}
@keyframes tailSw{from{transform:rotate(-10deg)}to{transform:rotate(12deg)}}
.blinkg{animation:blinkK 3.8s linear infinite}
@keyframes blinkK{0%,91%{transform:scaleY(1)}93%,95%{transform:scaleY(.12)}97%,100%{transform:scaleY(1)}}
.gtw1{animation:gtwK 3s ease-in-out infinite}
.gtw2{animation:gtwK 3s ease-in-out 1s infinite}
.gtw3{animation:gtwK 3s ease-in-out 2s infinite}
@keyframes gtwK{0%,100%{opacity:.5}50%{opacity:1}}
.flower{animation:sway 3.6s ease-in-out infinite alternate}
@keyframes sway{from{transform:rotate(-3deg)}to{transform:rotate(3deg)}}
""" + REDUCED

    body = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 110" width="900" height="110" role="img" aria-label="pixel cow-cat walking after a yarn ball">
<title>cow-cat divider</title>
<style>{css}</style>
<defs><clipPath id="frame"><rect x="0" y="0" width="900" height="110" rx="12"/></clipPath></defs>
<rect x="0" y="0" width="900" height="110" rx="12" fill="var(--bg)"/>
<g clip-path="url(#frame)">
  <rect x="140" y="26" width="8" height="8" rx="2" fill="var(--g2)" class="gtw1"/>
  <rect x="320" y="40" width="8" height="8" rx="2" fill="var(--g1)" class="gtw2"/>
  <rect x="520" y="22" width="8" height="8" rx="2" fill="var(--g3)" class="gtw3"/>
  <rect x="700" y="36" width="8" height="8" rx="2" fill="var(--g2)" class="gtw1"/>
  <rect x="830" y="30" width="8" height="8" rx="2" fill="var(--g1)" class="gtw2"/>

  <rect x="0" y="84" width="900" height="12.5" fill="var(--grass1)"/>
  <rect x="0" y="96" width="900" height="14" fill="var(--grass2)"/>
  <g fill="var(--tuft)">
    <g transform="translate(100,74)"><rect x="0" y="0" width="4" height="10"/><rect x="6" y="3" width="4" height="7"/></g>
    <g transform="translate(260,76)"><rect x="0" y="0" width="4" height="8"/><rect x="6" y="2" width="4" height="6"/></g>
    <g transform="translate(420,74)"><rect x="0" y="0" width="4" height="10"/><rect x="6" y="3" width="4" height="7"/></g>
    <g transform="translate(580,76)"><rect x="0" y="0" width="4" height="8"/><rect x="6" y="2" width="4" height="6"/></g>
    <g transform="translate(740,74)"><rect x="0" y="0" width="4" height="10"/><rect x="6" y="3" width="4" height="7"/></g>
    <g transform="translate(860,76)"><rect x="0" y="0" width="4" height="8"/><rect x="6" y="2" width="4" height="6"/></g>
  </g>
  <g transform="translate(200,64)"><g class="flower ob">{FLOWER.replace('__STEM__','8')}</g></g>
  <g transform="translate(640,64)"><g class="flower ob">{FLOWER.replace('__STEM__','8')}</g></g>

  <g class="catW"><g transform="translate(118,62) scale(.8)"><g class="rollW oc">{YARN_ART}</g></g></g>
  <g class="catW"><g class="bobW"><g transform="translate(0,29) scale(.8333)">{CAT_ART}</g></g></g>
</g>
</svg>"""
    return body

# ================================================================= write + render tests
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

files = {
    'cowcat-banner.svg': build_banner(),
    'cowcat-garden-3d.svg': build_garden(),
    'cowcat-divider.svg': build_divider(),
}
for name, content in files.items():
    with open(name, 'w') as f:
        f.write(content)
    print(name, len(content), 'bytes')

# flatten for cairosvg (no var()/media support) and render both themes
LIGHT = {}
DARK = {}
for blob, d in ((VARS_SHARED_LIGHT + VARS_FACES_LIGHT, LIGHT), (VARS_SHARED_DARK + VARS_FACES_DARK, DARK)):
    for line in blob.replace('\n', ' ').split(';'):
        line = line.strip()
        if line.startswith('--'):
            k, v = line.split(':', 1)
            d[k.strip()] = v.strip()

import cairosvg
for name in files:
    svg = open(name).read()
    for theme, tag in ((LIGHT, 'light'), (DARK, 'dark')):
        out = svg
        for k, v in theme.items():
            out = out.replace(f'var({k})', v)
        if tag == 'light':
            out = out.replace('<g class="night"', '<g visibility="hidden" class="night"', 1)
        else:
            out = out.replace('<g class="day"', '<g visibility="hidden" class="day"', 1)
        tmp = f'_t_{tag}_{name}'
        open(tmp, 'w').write(out)
        h = int(name and {'cowcat-banner.svg': 600, 'cowcat-garden-3d.svg': 600, 'cowcat-divider.svg': 220}[name])
        cairosvg.svg2png(url=tmp, write_to=f'_t_{tag}_{name}.png', output_width=1800, output_height=h)
print('rendered')
