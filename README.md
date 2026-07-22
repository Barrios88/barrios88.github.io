# Academic Website - John Manuel Barrios

## Overview
This is a professional academic website for John Manuel Barrios, Assistant Professor of Accounting at Yale School of Management. The website features a clean, modern design with thematic research organization and interactive paper pages.

## File Structure

```
Website/
├── index.html                          # Home page
├── research.html                       # Research page with thematic organization
├── cv.html                            # CV page with embedded PDF viewer
├── CV_John_2026_Version_Improved.pdf  # CV PDF file
├── photos/                            # Profile and other images
├── papers/                            # PDF files (named: YYYY-barrios-slug.pdf)
└── papers_web/                        # Interactive HTML pages for each paper
    ├── paper_licensing.html
    ├── paper_pe_accounting.html
    ├── paper_gig_economy.html
    ├── paper_hustling_home.html       # Hustling from Home? WFH and Entrepreneurial Entry
    ├── paper_civic_capital.html
    ├── paper_boards_feather.html
    ├── paper_risk_politics.html
    ├── paper_ridehailing.html
    ├── paper_tax_planning.html
    ├── paper_midnight_mergers.html
    ├── paper_misaligned_control.html
    ├── paper_staggered_did.html
    ├── paper_ai_disclosures.html
    ├── paper_regulatory_spillovers.html
    ├── paper_regulation_consensus.html
    ├── paper_measurement_matters.html
    ├── paper_ethics_illusions.html
    ├── paper_fraud_distance.html
    ├── paper_conflict_discount.html
    └── paper_accounting_pressure.html
```

## Design System

### Colors
- **Yale Blue**: `#00356b` - Primary brand color
- **Yale Orange**: `#bd5319` - Accent color
- **Cream**: `#f9f7f4` - Background for sections
- **White**: `#ffffff` - Primary background
- **Light Gray**: `#f8f9fa` - Subtle backgrounds

### Typography
- **Headings**: Crimson Pro (serif) - weights 400, 600, 700
- **Body Text**: Inter (sans-serif) - weights 400, 500, 600

### Icons
- Font Awesome 6.4.0 (solid icons)
- Globe icon (🌐) indicates papers with interactive pages

## Key Features Implemented

### 1. Navigation Structure
- Three main pages: Home, Research, CV
- Sticky navigation header on all pages
- Consistent navigation across all pages and paper pages

### 2. Research Page Organization
Papers are organized into **8 thematic categories**:
1. **Labor Markets & Employment** (briefcase icon)
2. **Entrepreneurship & Innovation** (rocket icon)
3. **Political Economy** (landmark icon)
4. **Corporate Governance** (users icon)
5. **Taxation & Regulatory Policy** (scale icon)
6. **Financial Reporting & Disclosure** (chart icon)
7. **Market Structure & Antitrust** (gavel icon)
8. **Ethics & Corporate Misconduct** (shield icon)

### 3. Interactive Paper Pages
- **20 papers** have dedicated interactive HTML pages (including *Hustling from Home?*)
- Each page features a **custom SVG network diagram** header
- Network diagram style with cream background (`#f9f7f4`)
- Consistent template across all papers
- Paper write-ups are aligned with actual PDF content and written in a direct, precise style (John Cochrane–style)

### 4. Globe Icon System
- Papers with interactive pages display a **globe icon (🌐)** next to the title
- Outlined circle design: white background with Yale blue border
- Hover effect: inverts to blue background with white icon
- "Paper Page" button in paper links section

### 5. CV Page
- Embedded PDF viewer for full CV
- Download button for PDF file
- Responsive iframe design

## Paper Page Template Structure

Each paper page in `papers_web/` follows this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paper Title - John Manuel Barrios</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@400;600;700&family=Inter:wght@400;500;600&display=swap">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* CSS variables and styles */
    </style>
</head>
<body>
    <!-- Sticky navigation -->
    <nav>
        <div class="nav-brand">John Manuel Barrios</div>
        <ul>
            <li><a href="../index.html">Home</a></li>
            <li><a href="../research.html">Research</a></li>
            <li><a href="../cv.html">CV</a></li>
        </ul>
    </nav>

    <!-- Paper header with SVG diagram -->
    <div class="paper-header">
        <svg class="network-svg" viewBox="0 0 800 200">
            <!-- Custom SVG network diagram for each paper -->
        </svg>
        <div class="paper-header-content">
            <h1>Paper Title</h1>
            <p class="authors">Authors</p>
            <p class="venue">Publication Venue</p>
        </div>
    </div>

    <!-- Main content -->
    <main>
        <!-- Abstract, key findings, sections -->
    </main>

    <!-- Footer with back button -->
    <footer>
        <div class="back-button">
            <a href="../research.html">← Back to Research</a>
        </div>
    </footer>
</body>
</html>
```

## How to Add a New Paper Page

### Step 1: Create the HTML File
1. Copy an existing paper page from `papers_web/` as a template
2. Name it following the pattern: `paper_[shortname].html`
3. Update the title, authors, venue, and content

### Step 2: Create a Custom SVG Diagram
Each paper should have a unique SVG that represents its theme:
- **Network connections**: Use circles and lines for social/organizational papers
- **Flow diagrams**: Use paths and arrows for process/change papers
- **Barriers/ladders**: Use geometric shapes for obstacle/progression papers
- **Diverging paths**: Use colored paths for polarization/choice papers

### Step 3: Update research.html
Add the globe icon and link to the paper:

```html
<div class="paper">
    <div class="paper-title">
        <a href="papers_web/paper_shortname.html">Paper Title</a>
        <a href="papers_web/paper_shortname.html" class="page-icon" title="View interactive paper page"><i class="fa-solid fa-globe"></i></a>
        <!-- Optional badges like <span class="badge badge-rr">R&R</span> -->
    </div>
    <div class="paper-authors">with Coauthors</div>
    <div class="paper-venue"><span class="journal-name">Journal Name</span>, Volume(Issue) (Year)</div>
    <div class="paper-links">
        <a class="paper-link" href="https://papers.ssrn.com/..." target="_blank"><i class="fa-solid fa-file-lines"></i> SSRN</a>
        <a class="paper-link" href="papers_web/paper_shortname.html"><i class="fa-solid fa-globe"></i> Paper Page</a>
    </div>
</div>
```

### Step 4: Place in the Right Theme Section
Add the paper to one of the 8 theme sections based on its research focus.

## CSS Classes Reference

### Research Page Classes
- `.theme-section` - Container for each thematic section
- `.theme-heading` - Section heading with icon
- `.paper` - Individual paper container
- `.paper-title` - Paper title with link
- `.page-icon` - Globe icon for papers with interactive pages
- `.paper-authors` - Author list
- `.paper-venue` - Publication venue
- `.paper-note` - Additional notes (e.g., "R&R", "Forthcoming")
- `.paper-links` - Container for SSRN, NBER, Paper Page links
- `.badge` - Status badges (R&R, Forthcoming, etc.)

### Paper Page Classes
- `.paper-header` - Hero section with SVG and title
- `.network-svg` - SVG diagram container
- `.paper-header-content` - Title, authors, venue overlay
- `.abstract-section` - Abstract text section
- `.key-findings` - Key findings/contributions section
- `.back-button` - Navigation back to research page

## Navigation Paths

### From Main Pages
- `index.html` → Root level
- `research.html` → Root level
- `cv.html` → Root level

### From Paper Pages
- Paper pages are in `papers_web/` subfolder
- Use `../` to navigate up to root:
  - `../index.html`
  - `../research.html`
  - `../cv.html`
  - `../papers/filename.pdf` (for PDF links)

## Responsive Design

All pages are responsive with breakpoints:
- **Desktop**: Full navigation, wide content
- **Tablet** (< 992px): Adjusted padding and spacing
- **Mobile** (< 768px): Stacked layout, larger touch targets

## External Dependencies

### Fonts
- Google Fonts: Crimson Pro, Inter
- Loaded via CDN in `<head>`

### Icons
- Font Awesome 6.4.0
- Loaded via CDN: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css`

### PDFs
- CV: `CV_John_2026_Version_Improved.pdf`
- Papers: Stored in `papers/` folder. **Naming convention**: `YYYY-barrios-slug.pdf` (e.g. `2024-barrios-hustling-home.pdf`, `2026-barrios-fraud-distance.pdf`). All HTML links use these filenames.

## Common Tasks

### Update CV
1. Replace `CV_John_2026_Version_Improved.pdf` with new PDF
2. Update filename reference in `cv.html` if name changes

### Add New Paper to Research Page
1. Find the appropriate theme section in `research.html`
2. Add paper using the structure shown above
3. If no interactive page exists, omit the globe icon

### Modify Colors
All colors are defined in CSS custom properties at the top of each file:
```css
:root {
    --yale-blue: #00356b;
    --yale-orange: #bd5319;
    --cream: #f9f7f4;
    --white: #ffffff;
}
```

### Update Navigation
Navigation is in the `<nav>` section at the top of each HTML file. Update all files for consistency.

## Current Status

✅ **Completed:**
- Home page with bio and contact info
- CV page with embedded PDF viewer
- Research page with 8 thematic sections
- 20 interactive paper pages with custom SVG diagrams
- Globe icon system for easy navigation
- Responsive design across all pages
- Consistent Yale branding throughout
- All paper PDFs in `papers/` use `YYYY-barrios-slug.pdf` naming; all paper pages link to these files and have working SSRN/NBER/Download PDF/Back to Research links

---

## Recent Changes (Session Notes for Future Chats)

**Use this section to bring a new assistant up to speed.**

### Paper write-ups aligned with PDFs (John Cochrane style)
- **`paper_fraud_distance.html`** (paper: `papers/WFH_and_Financial_Misconduct.pdf` → now `2026-barrios-fraud-distance.pdf`): Write-up was corrected to match the paper. The paper finds that firms *more able to work remotely* had **post-2020 declines** in financial misconduct (not increases). Mechanism: fraud is a **team/collusion** activity; remote work disrupts collusion (coordination costs, auditable channels). Cross-sectional: stronger declines in teamwork-intensive firms, effective internal controls, weaker pre-COVID culture. Detection lags fell; discretionary accruals declined. Diagram and text updated accordingly.
- **`paper_ethics_illusions.html`** (paper: `papers/Ethics_Noise.pdf` → now `2024-barrios-ethics-illusions.pdf`): Write-up was corrected to match the paper. Title in PDF is **"Ethics and Illusions: How Ethical Declarations Shape Market Behavior."** It is a **lab experiment**: seller reports before first-price auction; treatment = seller must sign ethical statement. Finding: signing **does not** reduce misreporting; it **shifts bidders’ beliefs** (more weight on reports, bid more aggressively), moving surplus to sellers. "Ethical noise" = belief shifts without behavior shifts. Abstract, key findings, diagram, and citation updated.

### Papers folder: naming and links
- All PDFs in `papers/` were **renamed** to `YYYY-barrios-slug.pdf` (e.g. `2021-barrios-boards-feather.pdf`, `2024-barrios-hustling-home.pdf`).
- **Duplicate PDFs removed**: `2024-barrios-ethics-illusions-alt.pdf`, `2022-barrios-cost-convenience-ridehailing-dup.pdf`.
- Every **paper page** in `papers_web/` that has a PDF was updated to link to the new filename (`../papers/YYYY-barrios-slug.pdf`).

### New paper page: Hustling from Home
- **`paper_hustling_home.html`** was added for "Hustling from Home? Work from Home Flexibility and Entrepreneurial Entry" (Barrios, Hochberg, Yi). NBER w33237, SSRN 5032374.
- **`research.html`** (and `research_backup.html`) were updated so the Hustling from Home entry links to this page and shows the globe icon and "Paper Page" link.
- User added the PDF to `papers/`; it was renamed to **`2024-barrios-hustling-home.pdf`**. The paper page was then filled with content from the PDF: abstract (WFH as natural experiment, substitution between employer flexibility and entrepreneurship, zip-code data, Startup Cartography Project, telework potential), key findings (substitution effect, internet/2SLS, "double deterrent" heterogeneity, gender-differential effects, survey evidence), research contribution, and Download PDF buttons.

### Paper links verified and completed
- Every paper page that has a PDF was checked: **all PDF links point to existing files** in `papers/`.
- **Bottom action blocks** on six paper pages were missing "Download PDF"; that button was added so both top and bottom blocks offer SSRN (or NBER/DOI where relevant), Download PDF, and Back to Research: `paper_midnight_mergers`, `paper_fraud_distance`, `paper_misaligned_control`, `paper_measurement_matters`, `paper_conflict_discount`, `paper_tax_planning`.

### Conventions to keep
- **Paper PDFs**: Store in `papers/` as `YYYY-barrios-slug.pdf`; link from paper pages as `../papers/YYYY-barrios-slug.pdf`.
- **New paper page**: Add `paper_shortname.html` in `papers_web/`, add entry in `research.html` with globe icon and "Paper Page" link, and ensure both top and bottom action blocks include Download PDF (if a PDF exists), SSRN/NBER/DOI as appropriate, and Back to Research.
- **Write-ups**: Match the actual paper (abstract, findings, mechanism). Prefer clear, precise prose (short sentences, "we find that…", "consistent with…") and correct direction of effects.

✅ **Earlier fixes (Feb 2026):**
- Paper pages use `../` for navigation and `../papers/` for PDFs so links work from the paper subfolder.
- Various paper pages had PDF paths and nav/back links fixed.

📋 **Future Enhancements (Optional):**
- Add more papers as they're published
- Create paper pages for remaining papers
- Add teaching page if needed
- Add media/press page if needed
- Include blog or commentary section

## Tips for Working with This Website

1. **Maintain Consistency**: Always use the established color scheme and typography
2. **SVG Diagrams**: Each paper's diagram should be unique and meaningful to the paper's content
3. **File Naming**: Paper pages: `paper_short_name.html`. PDFs in `papers/`: `YYYY-barrios-slug.pdf` (e.g. `2024-barrios-hustling-home.pdf`).
4. **Testing**: After updates, check all navigation links work correctly (top and bottom action blocks on each paper page).
5. **PDF Links**: All paper PDF links must point to `../papers/YYYY-barrios-slug.pdf`; those filenames are the single source of truth.

## Contact Information Display

The home page includes:
- Email: johnbarrios88@gmail.com
- Office: 165 Whitney Avenue
- Links to social/academic profiles (Twitter, Google Scholar, etc.)

Update these in `index.html` as needed.

---

**Last Updated**: February 2026  
**Website Version**: 2.0 (Thematic Organization + Interactive Paper Pages)  
**Session notes**: The "Recent Changes (Session Notes for Future Chats)" section above summarizes paper write-up corrections, PDF renaming, new Hustling from Home page, and link fixes so a new chat can continue from here.
