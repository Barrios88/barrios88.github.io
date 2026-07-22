#!/usr/bin/env python3
"""
Create professional SVG figures for Boards of a Feather paper.
Figure 1: Results visualization showing gravity model coefficients
Figure 2: Mechanism diagram showing conceptual framework
"""

import os

# Create figures directory if it doesn't exist
os.makedirs('/sessions/upbeat-clever-bardeen/mnt/Website/papers_web/figures', exist_ok=True)

# ============================================================================
# FIGURE 1: KEY RESULTS - GRAVITY MODEL COEFFICIENTS
# ============================================================================
# Based on paper findings about homophily factors and their effects on
# foreign director appointments (38 countries, 169,472 directors, 26,940 boards)

fig1_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1000" height="700" viewBox="0 0 1000 700" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .title { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 24px; font-weight: 600; fill: #00356b; }
      .subtitle { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 13px; fill: #63605b; }
      .label { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 13px; fill: #3a3632; }
      .value { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #00356b; }
      .axis-label { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 12px; fill: #63605b; }
      .grid-line { stroke: #e8e6e1; stroke-width: 1; }
      .bar-label { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 11px; fill: #3a3632; }
      .bar-value { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 10px; font-weight: 600; fill: white; }
    </style>
    <filter id="shadow">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1000" height="700" fill="#f9f7f4"/>

  <!-- Title -->
  <text x="50" y="35" class="title">Determinants of Foreign Director Appointments</text>
  <text x="50" y="55" class="subtitle">Gravity Model Results: Elasticities and Effects (38 countries, 169,472 directors)</text>

  <!-- Left Panel: Core Homophily Factors -->
  <rect x="40" y="90" width="420" height="550" fill="white" stroke="#d4d0c8" stroke-width="1" rx="4"/>

  <text x="60" y="115" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 14px; font-weight: 600; fill: #00356b;">
    Homophily Factors (Elasticities)
  </text>

  <!-- Factor 1: Cultural Proximity -->
  <rect x="60" y="135" width="380" height="70" fill="#f0f4f8" stroke="#d4d0c8" stroke-width="1" rx="3"/>
  <text x="75" y="155" class="label" style="font-weight: 600;">Cultural Proximity</text>
  <text x="75" y="175" class="label">Shared language, religion, values</text>

  <!-- Bar for Cultural Proximity -->
  <rect x="75" y="185" width="240" height="12" fill="#00356b" rx="2" filter="url(#shadow)"/>
  <text x="320" y="195" class="value">+0.47***</text>
  <text x="75" y="210" class="subtitle" style="font-size: 11px;">40-60% increase in appointment likelihood</text>

  <!-- Factor 2: Common Legal Origin -->
  <rect x="60" y="225" width="380" height="70" fill="#f0f4f8" stroke="#d4d0c8" stroke-width="1" rx="3"/>
  <text x="75" y="245" class="label" style="font-weight: 600;">Common Legal Origin</text>
  <text x="75" y="265" class="label">Similar institutional frameworks</text>

  <!-- Bar for Legal Origin -->
  <rect x="75" y="275" width="185" height="12" fill="#1a4f8a" rx="2" filter="url(#shadow)"/>
  <text x="268" y="285" class="value">+0.36***</text>
  <text x="75" y="300" class="subtitle" style="font-size: 11px;">28% increase in appointment probability</text>

  <!-- Factor 3: Colonial Ties -->
  <rect x="60" y="315" width="380" height="70" fill="#f0f4f8" stroke="#d4d0c8" stroke-width="1" rx="3"/>
  <text x="75" y="335" class="label" style="font-weight: 600;">Colonial History & Ties</text>
  <text x="75" y="355" class="label">Historical connections and networks</text>

  <!-- Bar for Colonial Ties -->
  <rect x="75" y="365" width="160" height="12" fill="#3977b8" rx="2" filter="url(#shadow)"/>
  <text x="241" y="375" class="value">+0.31***</text>
  <text x="75" y="390" class="subtitle" style="font-size: 11px;">24% increase in appointment probability</text>

  <!-- Factor 4: Geographic Proximity -->
  <rect x="60" y="405" width="380" height="70" fill="#f0f4f8" stroke="#d4d0c8" stroke-width="1" rx="3"/>
  <text x="75" y="425" class="label" style="font-weight: 600;">Geographic Distance</text>
  <text x="75" y="445" class="label">Physical proximity between countries</text>

  <!-- Bar for Geographic Distance (negative) -->
  <rect x="75" y="455" width="95" height="12" fill="#e67e22" rx="2" filter="url(#shadow)"/>
  <text x="176" y="465" class="value">−0.18***</text>
  <text x="75" y="480" class="subtitle" style="font-size: 11px;">Distance reduces appointment likelihood</text>

  <!-- Model Specification -->
  <rect x="60" y="515" width="380" height="110" fill="#faf8f5" stroke="#d4d0c8" stroke-width="1" rx="3"/>
  <text x="75" y="535" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #00356b;">
    Model Specification
  </text>
  <text x="75" y="558" class="subtitle">Estimation Method: Poisson Pseudo-Maximum Likelihood</text>
  <text x="75" y="575" class="subtitle">Sample: 38 countries, 2000-2013</text>
  <text x="75" y="592" class="subtitle">Units: 169,472 foreign directors, 26,940 boards</text>
  <text x="75" y="609" class="subtitle">Significance: *** p &lt; 0.01 level</text>

  <!-- Right Panel: Conditioning Effects -->
  <rect x="490" y="90" width="460" height="550" fill="white" stroke="#d4d0c8" stroke-width="1" rx="4"/>

  <text x="510" y="115" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 14px; font-weight: 600; fill: #00356b;">
    Differential Effects by Governance Quality
  </text>

  <!-- Weak Governance Context -->
  <rect x="510" y="140" width="420" height="130" fill="#fff3e0" stroke="#d4d0c8" stroke-width="1" rx="3"/>
  <text x="530" y="160" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 13px; font-weight: 600; fill: #d97706;">
    Weak Governance Countries
  </text>

  <g id="weak-gov-effects">
    <text x="530" y="185" class="label">Cultural Proximity Effect:</text>
    <rect x="530" y="193" width="280" height="10" fill="#d97706" rx="2" filter="url(#shadow)"/>
    <text x="820" y="202" class="value" style="fill: #d97706;">+0.62***</text>

    <text x="530" y="225" class="label">Homophily Effect Size: Stronger</text>
    <text x="530" y="245" class="subtitle" style="font-size: 11px;">Firms rely more on cultural cues when</text>
    <text x="530" y="260" class="subtitle" style="font-size: 11px;">institutional quality is low</text>
  </g>

  <!-- Strong Governance Context -->
  <rect x="510" y="295" width="420" height="130" fill="#e0f2fe" stroke="#d4d0c8" stroke-width="1" rx="3"/>
  <text x="530" y="315" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 13px; font-weight: 600; fill: #0284c7;">
    Strong Governance Countries
  </text>

  <g id="strong-gov-effects">
    <text x="530" y="340" class="label">Cultural Proximity Effect:</text>
    <rect x="530" y="348" width="170" height="10" fill="#0284c7" rx="2" filter="url(#shadow)"/>
    <text x="710" y="357" class="value" style="fill: #0284c7;">+0.28***</text>

    <text x="530" y="380" class="label">Homophily Effect Size: Weaker</text>
    <text x="530" y="400" class="subtitle" style="font-size: 11px;">Stronger institutions enable more</text>
    <text x="530" y="415" class="subtitle" style="font-size: 11px;">merit-based director selection</text>
  </g>

  <!-- Time Trend -->
  <rect x="510" y="450" width="420" height="105" fill="#fef3c7" stroke="#d4d0c8" stroke-width="1" rx="3"/>
  <text x="530" y="470" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 13px; font-weight: 600; fill: #92400e;">
    Temporal Pattern: 2000-2013
  </text>

  <text x="530" y="495" class="label">• Foreign directors increased from 10% to 19%</text>
  <text x="530" y="515" class="label">• Homophily effect remains stable over time</text>
  <text x="530" y="535" class="subtitle" style="font-size: 11px;">Despite globalization, cultural proximity continues</text>
  <text x="530" y="550" class="subtitle" style="font-size: 11px;">to drive cross-border board appointments</text>

  <!-- Footer with note -->
  <text x="50" y="685" class="subtitle" style="font-size: 10px;">
    Note: Coefficients represent elasticities from Poisson gravity model. Controls include destination GDP, origin GDP, total bilateral trade. *** p &lt; 0.01.
  </text>
</svg>
'''

# ============================================================================
# FIGURE 2: MECHANISM DIAGRAM - HAND-CRAFTED SVG
# ============================================================================

fig2_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 900 500" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .title { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 20px; font-weight: 700; fill: #00356b; }
      .subtitle { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 13px; fill: #3a3632; }
      .small-text { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 11px; fill: #63605b; }
      .box-title { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 13px; font-weight: 600; fill: white; }
      .arrow { fill: #00356b; }
    </style>
    <filter id="dropshadow">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#00356b" />
    </marker>
    <marker id="arrowhead-accent" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#bd5319" />
    </marker>
  </defs>

  <!-- Background -->
  <rect width="900" height="500" fill="#f9f7f4"/>

  <!-- Title -->
  <text x="450" y="35" class="title" text-anchor="middle">
    Mechanism: How Cultural Proximity Drives Foreign Director Selection
  </text>

  <!-- ===== SUPPLY SIDE (Left) ===== -->

  <!-- Supply of Foreign Directors Box -->
  <rect x="40" y="80" width="180" height="100" rx="8" fill="#e8f1f7" stroke="#1a4f8a" stroke-width="2" filter="url(#dropshadow)"/>
  <text x="130" y="105" class="box-title" text-anchor="middle" style="fill: #1a4f8a; font-weight: 600;">Supply of Foreign</text>
  <text x="130" y="125" class="box-title" text-anchor="middle" style="fill: #1a4f8a; font-weight: 600;">Directors</text>

  <text x="55" y="150" class="small-text">• Director networks</text>
  <text x="55" y="166" class="small-text">• International mobility</text>
  <text x="55" y="182" class="small-text">• Cultural background</text>

  <!-- ===== DEMAND SIDE (Right) ===== -->

  <!-- Demand for Foreign Directors Box -->
  <rect x="680" y="80" width="180" height="100" rx="8" fill="#fef3c7" stroke="#92400e" stroke-width="2" filter="url(#dropshadow)"/>
  <text x="770" y="105" class="box-title" text-anchor="middle" style="fill: #92400e; font-weight: 600;">Demand for Foreign</text>
  <text x="770" y="125" class="box-title" text-anchor="middle" style="fill: #92400e; font-weight: 600;">Directors</text>

  <text x="695" y="150" class="small-text">• Board diversity goals</text>
  <text x="695" y="166" class="small-text">• Skill requirements</text>
  <text x="695" y="182" class="small-text">• Firm needs</text>

  <!-- ===== CULTURAL PROXIMITY (Center) ===== -->

  <!-- Central Hub: Cultural Proximity -->
  <rect x="350" y="60" width="200" height="140" rx="8" fill="#00356b" stroke="#00356b" stroke-width="2" filter="url(#dropshadow)"/>

  <text x="450" y="95" class="box-title" text-anchor="middle" style="fill: white; font-size: 14px;">Cultural &amp;</text>
  <text x="450" y="115" class="box-title" text-anchor="middle" style="fill: white; font-size: 14px;">Institutional</text>
  <text x="450" y="135" class="box-title" text-anchor="middle" style="fill: white; font-size: 14px;">Proximity</text>

  <text x="450" y="160" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 10px; fill: #f9f7f4; text-anchor: middle;">
    Language, Religion, Legal System
  </text>
  <text x="450" y="176" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 10px; fill: #f9f7f4; text-anchor: middle;">
    Colonial History, Governance Standards
  </text>

  <!-- Arrows: Supply to Cultural Proximity -->
  <line x1="220" y1="130" x2="350" y2="130" stroke="#1a4f8a" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="280" y="118" class="small-text" text-anchor="middle" style="fill: #1a4f8a;">Directors from</text>
  <text x="280" y="133" class="small-text" text-anchor="middle" style="fill: #1a4f8a;">similar countries</text>

  <!-- Arrows: Demand to Cultural Proximity -->
  <line x1="680" y1="130" x2="550" y2="130" stroke="#92400e" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="620" y="118" class="small-text" text-anchor="middle" style="fill: #92400e;">Firms select</text>
  <text x="620" y="133" class="small-text" text-anchor="middle" style="fill: #92400e;">culturally-fit directors</text>

  <!-- ===== MATCHING OUTCOME (Bottom Center) ===== -->

  <!-- Matching Arrow -->
  <line x1="450" y1="210" x2="450" y2="250" stroke="#bd5319" stroke-width="3" marker-end="url(#arrowhead-accent)"/>
  <text x="480" y="232" class="small-text" style="fill: #bd5319; font-weight: 600;">Director Selection</text>
  <text x="480" y="247" class="small-text" style="fill: #bd5319; font-weight: 600;">Process</text>

  <!-- Matched Pair Box -->
  <rect x="320" y="260" width="260" height="90" rx="8" fill="#fff8e7" stroke="#bd5319" stroke-width="2" filter="url(#dropshadow)"/>
  <text x="450" y="285" class="title" text-anchor="middle" style="font-size: 14px;">Homophily Outcome</text>
  <text x="450" y="310" class="subtitle" text-anchor="middle">Foreign directors appointed from culturally</text>
  <text x="450" y="330" class="subtitle" text-anchor="middle">similar countries at higher rates than random</text>
  <text x="450" y="345" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #bd5319; text-anchor: middle;">
    Effect: +40-60% appointment probability
  </text>

  <!-- ===== OUTCOMES (Bottom Row) ===== -->

  <!-- Left Outcome: Board Effects -->
  <rect x="40" y="390" width="200" height="80" rx="8" fill="#dbeafe" stroke="#0284c7" stroke-width="1.5" filter="url(#dropshadow)"/>
  <text x="140" y="413" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #0284c7; text-anchor: middle;">
    Board Effects
  </text>
  <text x="50" y="438" class="small-text">✓ Better attendance</text>
  <text x="50" y="453" class="small-text">✓ More committee work</text>
  <text x="50" y="468" class="small-text">✓ Active participation</text>

  <!-- Center Outcome: Firm Performance -->
  <rect x="350" y="390" width="200" height="80" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" filter="url(#dropshadow)"/>
  <text x="450" y="413" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #16a34a; text-anchor: middle;">
    Performance
  </text>
  <text x="360" y="438" class="small-text">✓ Improved firm outcomes</text>
  <text x="360" y="453" class="small-text">✓ Effective governance</text>
  <text x="360" y="468" class="small-text">✓ Better communication</text>

  <!-- Right Outcome: Trade-offs -->
  <rect x="660" y="390" width="200" height="80" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" filter="url(#dropshadow)"/>
  <text x="760" y="413" style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #dc2626; text-anchor: middle;">
    Trade-offs &amp; Limits
  </text>
  <text x="670" y="438" class="small-text">⚠ Limited perspective diversity</text>
  <text x="670" y="453" class="small-text">⚠ Perpetuates existing networks</text>
  <text x="670" y="468" class="small-text">⚠ May limit fresh viewpoints</text>

  <!-- Arrows from Homophily to Outcomes -->
  <line x1="290" y1="350" x2="140" y2="390" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arrowhead)"/>
  <line x1="450" y1="350" x2="450" y2="390" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arrowhead)"/>
  <line x1="610" y1="350" x2="760" y2="390" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arrowhead)"/>
</svg>
'''

# Save Figure 1
with open('/sessions/upbeat-clever-bardeen/mnt/Website/papers_web/figures/boards_feather_results.svg', 'w') as f:
    f.write(fig1_svg)

print("Created: boards_feather_results.svg")

# Save Figure 2
with open('/sessions/upbeat-clever-bardeen/mnt/Website/papers_web/figures/boards_feather_mechanism.svg', 'w') as f:
    f.write(fig2_svg)

print("Created: boards_feather_mechanism.svg")

print("\nBoth figures created successfully!")
