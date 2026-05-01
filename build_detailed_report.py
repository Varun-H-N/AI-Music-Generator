from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.sax.saxutils import escape


OUTPUT = Path("AI_Music_Generator_Detailed_Report.docx")


REPORT_STRUCTURE = [
    {
        "type": "title_page",
        "title": "AI MUSIC GENERATOR",
        "subtitle": "Detailed Project Report",
        "details": [
            "Prepared from complete project analysis of the Flask-based AI Music Generator.",
            "Formatting: Times New Roman, chapter titles 18 pt, subtopics 14 pt, body text 12 pt, line spacing 1.5.",
            "Chapter structure aligned to the six chapters provided by the user from the reference PDF.",
        ],
    },
    {
        "type": "page",
        "title": "ABSTRACT",
        "sections": [
            {
                "heading": "Project Summary",
                "paragraphs": [
                    "The AI Music Generator is a web-based application that creates short genre-oriented music tracks automatically according to a user selection. The project combines a lightweight Flask backend, a browser-based interface, and a procedural audio generation engine implemented in Python. Instead of relying on a heavy neural model or external music-generation service, the system uses waveform synthesis, tempo mapping, randomized note selection, amplitude envelopes, and optional percussion textures to create downloadable WAV audio files on demand.",
                    "The project is valuable as an academic report topic because it combines ideas from generative artificial intelligence, signal processing, and full-stack web development in one understandable system. A user selects a genre such as happy, sad, romance, action, thriller, EDM, rock, jazz, lo-fi, ambient, hip-hop, cinematic, piano, horror, or sci-fi. The backend then creates ten unique audio outputs for that genre and returns them to the webpage with playback controls and download links.",
                    "This report is based on a full review of the project source files including app.py, generate_music.py, templates/index.html, and templates/player.html. It explains the motivation behind the project, describes the architecture and working logic, discusses implementation choices, evaluates the generated outputs, and concludes with future improvements. The report uses the six-chapter structure requested by the user and the formatting style specified for submission in Word format.",
                ],
            }
        ],
    },
    {
        "type": "toc",
        "title": "TABLE OF CONTENTS",
        "entries": [
            "Abstract",
            "Chapter 1 - Introduction",
            "Chapter 2 - Background and Motivation",
            "Chapter 3 - System Architecture",
            "Chapter 4 - Implementation",
            "Chapter 5 - Results and Testing",
            "Chapter 6 - Conclusion and Future Work",
            "References",
        ],
    },
    {
        "type": "page",
        "title": "CHAPTER 1 - INTRODUCTION",
        "sections": [
            {
                "heading": "Introduction to Generative Music Systems",
                "paragraphs": [
                    "Artificial intelligence has significantly expanded the possibilities of creative computing. Systems can now generate text, images, code, speech, and music with increasing sophistication. Music generation is especially interesting because it combines artistic intent with mathematical structure. A music generation system must make decisions about tempo, pitch, rhythm, layering, and continuity over time. Even a small prototype can therefore demonstrate important ideas from AI, digital signal processing, and interactive software design.",
                    "The AI Music Generator project explores this area through a lightweight and procedural approach. Instead of requiring model training, expensive hardware, or external APIs, it generates music locally by creating synthetic audio signals according to musical rules and random variation. This makes the system easier to understand, easier to demonstrate, and more suitable for an academic project report where the internal logic must be explained clearly during evaluation or viva discussion.",
                    "The project is implemented as a Flask application so that users can access the generator through a web browser. The interface allows the user to choose a genre, trigger audio generation, listen to the results directly, and download the generated tracks. This creates a complete workflow from user input to generated output, making the project much more meaningful than a standalone script because it demonstrates both creative logic and software integration.",
                ],
            },
            {
                "heading": "Objectives and Scope of the Project",
                "paragraphs": [
                    "The first objective of the project is to provide an accessible music-generation tool that can create multiple outputs from a simple genre selection. The second objective is to demonstrate how generative AI concepts can be implemented through procedural rules without requiring deep learning. The third objective is to connect frontend interaction, backend request handling, and audio synthesis into one integrated application that is easy to present and explain.",
                    "The project is intentionally scoped as a mini-project. It focuses on genre-based music generation using synthesized waveforms and local WAV-file export. It does not train on large datasets, model real instruments, or create full commercial-quality compositions. The purpose is not to replace professional audio production but to show how automated music creation can be achieved through a structured and educational implementation.",
                    "Because of this scope, the project becomes a strong learning platform. It introduces concepts such as routing, templates, client-server interaction, file generation, waveform mathematics, randomization, and audio normalization. These are all useful technical themes for academic documentation and software demonstration.",
                ],
            },
        ],
    },
    {
        "type": "page",
        "title": "CHAPTER 2 - BACKGROUND AND MOTIVATION",
        "sections": [
            {
                "heading": "Background of Generative AI in Music",
                "paragraphs": [
                    "Generative AI refers to systems that produce new content automatically rather than only analyzing existing data. In music, generation can take many forms: symbolic note generation, MIDI composition, accompaniment creation, rhythm synthesis, or raw audio waveform production. Recent industry systems often rely on transformer-based architectures, diffusion models, or other data-driven approaches trained on very large datasets. These systems can generate highly polished output, but they are often complex, computationally expensive, and difficult to explain in full from the perspective of a small academic project.",
                    "Procedural generation remains an important alternative in educational settings. In procedural systems, content is created through rules, parameters, patterns, and randomness. This approach is transparent and efficient because the developer can trace exactly how the output is constructed. For students, this is highly useful because each design decision can be mapped directly to the behavior of the final system. The AI Music Generator follows this procedural philosophy by controlling tempo, note selection, harmonic layering, and drum behavior according to genre-specific logic.",
                    "The project therefore fits within the broader generative AI domain even though it is not based on deep learning. It demonstrates a practical principle: intelligent content generation can be implemented through structured algorithmic design when the project goal is explainability, controllability, and educational value.",
                ],
            },
            {
                "heading": "Motivation Behind the Project",
                "paragraphs": [
                    "Many users need short mood-based background tracks for demonstrations, presentations, small videos, classroom prototypes, or creative experimentation. However, manual music production usually requires musical knowledge, experience with instruments or digital audio workstations, and significant time investment. This creates a barrier for students and beginners who simply need a quick way to generate suitable audio.",
                    "The project is motivated by the idea that music generation should be made approachable. By allowing a user to choose a genre and automatically receive ten generated outputs, the system reduces the creative and technical barrier to entry. It also gives learners an example of how software can convert high-level user input into tangible multimedia output.",
                    "Another major motivation is academic demonstration. A project like this is attractive because it connects theory and implementation. It allows discussion of AI concepts, mathematics of waveforms, web programming, software structure, testing, and future scope in one cohesive report. That combination makes it a strong final-year or mini-project topic.",
                ],
            },
        ],
    },
    {
        "type": "page",
        "title": "CHAPTER 3 - SYSTEM ARCHITECTURE",
        "sections": [
            {
                "heading": "Overall Architecture",
                "paragraphs": [
                    "The AI Music Generator follows a simple client-server architecture. The frontend is built with HTML, CSS, and JavaScript inside Flask templates. The backend is implemented in Python using Flask. The audio-generation engine is separated into its own module, generate_music.py, which allows the project to divide presentation logic, application routing, and synthesis behavior into clear units.",
                    "When a user visits the root route, the Flask server renders the index template with no song list. The user interacts with genre cards on the webpage and selects one of the supported styles. When the form is submitted, a POST request is sent to the /generate route. That route reads the selected genre, passes it to the generation module, receives a list of created filenames, and renders the same template again with the generated music data and the appropriate background image.",
                    "This structure supports clarity and maintainability. The webpage is responsible only for user interaction and result presentation. Flask handles request flow and context passing. The synthesis engine focuses entirely on constructing audio. Such separation is valuable for both software quality and report writing because each layer can be analyzed independently.",
                ],
            },
            {
                "heading": "Module Analysis",
                "paragraphs": [
                    "The first important module is app.py. This file initializes the Flask application, defines the supported genre-to-image mapping, and registers the two main routes. The home route loads the application with no generated songs, while the generate route accepts form input and triggers the backend generation process. This file is the central coordinator of user requests and response rendering.",
                    "The second major module is generate_music.py. This file contains the audio synthesis logic. It defines a sample rate, helper functions for sine-wave generation, amplitude envelopes, and drum-like sound creation. It also sets genre-based tempo rules, selects musical scales, chooses frequencies randomly, layers bass and melody elements, and saves normalized output as WAV files. This is the algorithmic core of the application.",
                    "The third important module is the frontend template in templates/index.html. This file presents the user interface, including the title, genre grid, submission button, loading message, and output display with audio players. It also contains client-side JavaScript for selecting a genre, visually highlighting the current choice, and updating the background image before submission. Together, these modules create a complete and understandable architecture.",
                ],
            },
            {
                "heading": "Data and Control Flow",
                "paragraphs": [
                    "The control flow begins in the browser. A user selects a genre card, and JavaScript writes that genre into a hidden form field. The same script updates the background image and highlights the selected card so the user receives immediate visual feedback. Once the user clicks the generate button, the form sends the selected value to Flask through an HTTP POST request.",
                    "The Flask backend receives the genre and invokes the generate_music function. That function creates or confirms the output directory, clears previously generated files, builds ten new songs, writes them into the static music folder, and returns the list of filenames. Flask then injects those filenames into the template context, allowing the browser to display playback and download controls for each result.",
                    "This flow is an example of clean client-server integration. A small input from the user travels through the interface, backend, and generation engine before returning as an interactive media output. The architecture is therefore simple in design but complete in execution.",
                ],
            },
        ],
    },
    {
        "type": "page",
        "title": "CHAPTER 4 - IMPLEMENTATION",
        "sections": [
            {
                "heading": "Frontend Implementation",
                "paragraphs": [
                    "The user interface is implemented primarily in templates/index.html. The page uses a simple grid of genre cards so that the user can quickly choose a style of music. Styling is embedded directly in the template using CSS. The design includes a full-page background image, a dark overlay for readability, a centered title, interactive genre cards, a generation button, and a loader message. Generated songs appear below the form, each with a browser-native audio player and a direct download link.",
                    "JavaScript inside the template controls user interaction. The selectGenre function stores the chosen genre in a hidden input field, updates the selected card color, and changes the page background according to the genre image map. Another function shows a loading message when the form is submitted. This client-side behavior improves the user experience without adding unnecessary complexity.",
                    "An additional template, templates/player.html, exists as a simpler output page. Although the main workflow uses index.html for combined input and output, the alternate template shows the project’s development pattern and demonstrates another way to render generated songs.",
                ],
            },
            {
                "heading": "Backend and Audio Generation Logic",
                "paragraphs": [
                    "The backend implementation in app.py is compact but effective. A dictionary called genre_images maps each music genre to a corresponding image URL. This allows the selected genre to influence both the audio output and the visual theme of the webpage. The generate route accepts the submitted genre, calls the generator, and returns the results to the template in a single cycle, which keeps the user workflow straightforward.",
                    "The actual synthesis process is implemented in generate_music.py. The sample rate is set to 44100 Hz, a standard rate for digital audio. The sine function produces a pure waveform using the standard trigonometric formula based on frequency and time. The envelope function applies gradual fade-in and fade-out behavior so that individual segments sound smoother and avoid abrupt clipping or clicking. A drum helper creates noise-based percussive texture with exponential decay.",
                    "The generate_music function begins by ensuring that the static output folder exists. It then deletes previous songs from that folder so that the new generation cycle contains only fresh outputs. A tempo map defines beats per minute for each genre. The generator converts tempo into beat length and uses that timing reference when building each audio segment.",
                ],
            },
            {
                "heading": "Algorithmic Working in Detail",
                "paragraphs": [
                    "For each generation request, the system creates ten songs. Each song starts with a randomly selected scale and a random number of steps. For every step, the program determines a segment duration and generates a time vector using NumPy. In most genres, it then chooses a base frequency from the selected scale and combines it with harmonic variations such as major, minor, or power-style layering. Bass and melody components are added using additional frequencies derived from the base note.",
                    "Genre-specific logic influences the result. Romance uses a more restricted and softer note set with reduced harmonic intensity so that the output avoids harsh, siren-like tones. Genres such as action, EDM, rock, and hip-hop are more likely to receive drum-like texture, while calm genres such as sad, lo-fi, ambient, and piano remain softer and less percussive. Thriller and sci-fi apply percussion more sparingly to retain a tense atmosphere.",
                    "After segment construction, the envelope is applied to smooth the edges. In several soft genres, the signal is passed through the hyperbolic tangent function to soften peaks. All segments are concatenated into one waveform, normalized to the 16-bit PCM range, converted to integer values, and written as WAV files using SciPy. Filenames are created with UUIDs so that each generated file is uniquely named.",
                ],
            },
        ],
    },
    {
        "type": "page",
        "title": "CHAPTER 5 - RESULTS AND TESTING",
        "sections": [
            {
                "heading": "Testing Approach",
                "paragraphs": [
                    "Testing for the AI Music Generator is primarily functional and output-oriented. The first level of testing checks whether the Flask server starts correctly and renders the main page without template errors. The second level verifies whether genre selection works properly, meaning the selected value is captured in the hidden form field and submitted to the backend route. The third level confirms that the generation route successfully creates audio files and returns them for display.",
                    "Another key part of testing is file verification. Each generation cycle should produce ten WAV files in the static music directory. The files should be playable in the browser through the audio controls and downloadable through the provided links. Since the project generates synthetic sound rather than text or images, listening-based verification is also important. The evaluator must confirm that genre outputs sound different enough to reflect the intended tempo and energy changes.",
                    "User-interface testing is also relevant. The loader message should appear when generation begins, genre highlighting should work correctly, and the selected background image should update according to the chosen style. These interface behaviors improve the usability and presentation quality of the project.",
                ],
            },
            {
                "heading": "Observed Results",
                "paragraphs": [
                    "The project successfully generates ten audio files for each genre request. Because the generation process uses randomness, no two runs are exactly identical, which is a desirable property for a creative system. The audio results are clearly synthetic, but they still show recognizable mood differences. Faster genres tend to produce more energetic and rhythmically active output, while slower genres produce smoother and calmer sound patterns.",
                    "The project’s frontend and backend integration also behaves correctly. The songs are displayed immediately after generation, and each file can be played and downloaded from the webpage. This confirms that the application does not only generate audio but also delivers it to the user in a usable way. That end-to-end success is an important result because it shows the system working as a complete web application rather than a disconnected script.",
                    "From an educational point of view, the result validates the project objective. The application demonstrates that procedural generation techniques can create genre-aware audio in an understandable and interactive form. It also proves that a small codebase can meaningfully connect AI-inspired logic with real output generation and user interaction.",
                ],
            },
            {
                "heading": "Strengths, Limitations, and Interpretation",
                "paragraphs": [
                    "One clear strength of the results is consistency of workflow. The system repeatedly accepts input, generates new content, and presents it back to the user with minimal delay. Another strength is explainability. Since the output is generated through visible rules instead of a black-box model, it is easier to justify why a certain genre sounds faster, softer, or more percussive.",
                    "At the same time, the output remains limited when compared with advanced music-generation systems. The generated audio lacks realistic instruments, long-range composition structure, and highly refined harmony. It is better understood as synthetic genre-inspired sound rather than polished commercial music. However, this limitation is acceptable within the project’s scope because the main purpose is educational demonstration and not production-grade composition.",
                    "Overall, the testing results show that the project is successful on its own terms. It meets the core goals of automation, genre-based variation, output generation, playback, and download, while remaining compact enough to be fully understood and documented.",
                ],
            },
        ],
    },
    {
        "type": "page",
        "title": "CHAPTER 6 - CONCLUSION AND FUTURE WORK",
        "sections": [
            {
                "heading": "Conclusion",
                "paragraphs": [
                    "The AI Music Generator is a successful academic mini-project that demonstrates how generative AI concepts can be implemented through a procedural audio system. The project combines Flask-based request handling, HTML and JavaScript interface design, NumPy-based waveform generation, and SciPy-based file writing into one integrated application. The result is a system that accepts a simple user choice and converts it into multiple playable and downloadable music outputs.",
                    "The project’s strongest quality is its balance between simplicity and substance. The codebase is small enough to analyze completely, but it still covers several important technical areas such as routing, signal generation, interface design, randomization, file handling, and multimedia delivery. This makes it highly suitable for project submission, viva explanation, and technical discussion.",
                    "The project also demonstrates a broader lesson in artificial intelligence: meaningful content generation does not always require large opaque models. In many educational scenarios, a transparent rule-based system can be more effective because it allows deeper understanding of how the output is produced.",
                ],
            },
            {
                "heading": "Future Work",
                "paragraphs": [
                    "There are many directions in which the project can be extended. The application could allow users to control duration, tempo, note density, percussion strength, or instrument mood. It could preserve previously generated songs instead of deleting them, and it could organize outputs into user-specific or timestamped folders for better history tracking.",
                    "The system could also be improved by supporting MIDI export, waveform visualization, and more advanced music structures such as intros, loops, verse-like patterns, or layered instruments. On the interface side, the design could be made more responsive for mobile screens and enhanced with better state handling, previews, and playlist-style controls.",
                    "For a more advanced AI direction, a future version could combine this procedural framework with machine-learning models. A transformer or symbolic melody generator could provide note sequences, while the existing system could handle rendering or arrangement. Prompt-based generation, where the user enters natural-language requests such as calm rainy piano or futuristic chase soundtrack, would also make the system more expressive and modern.",
                ],
            },
        ],
    },
    {
        "type": "page",
        "title": "REFERENCES",
        "sections": [
            {
                "heading": "Reference Sources Used for the Report",
                "paragraphs": [
                    "1. Source file analysis of app.py for Flask routing, request handling, and genre-to-image mapping.",
                    "2. Source file analysis of generate_music.py for waveform synthesis, envelope processing, tempo rules, and WAV-file generation.",
                    "3. Source file analysis of templates/index.html for interface layout, style, JavaScript interaction, and output rendering.",
                    "4. Source file analysis of templates/player.html for alternate playback-page structure.",
                    "5. Standard Python modules used in the project, including os, random, time, and uuid.",
                    "6. NumPy usage for numerical array operations in sound generation.",
                    "7. SciPy wavfile writing utilities for exporting final audio data.",
                    "8. Chapter titles provided by the user from the uploaded reference PDF named Gen AI Full report.pdf.",
                ],
            }
        ],
    },
]


def ppr(line_spacing: int = 360, before: int = 0, after: int = 120, center: bool = False) -> str:
    jc = '<w:jc w:val="center"/>' if center else ""
    return (
        "<w:pPr>"
        f"<w:spacing w:before=\"{before}\" w:after=\"{after}\" w:line=\"{line_spacing}\" w:lineRule=\"auto\"/>"
        f"{jc}"
        "</w:pPr>"
    )


def rpr(size_half_points: int, bold: bool = False, italic: bool = False) -> str:
    return (
        "<w:rPr>"
        '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
        + ("<w:b/>" if bold else "")
        + ("<w:i/>" if italic else "")
        + f'<w:sz w:val="{size_half_points}"/>'
        + f'<w:szCs w:val="{size_half_points}"/>'
        + "</w:rPr>"
    )


def paragraph(
    text: str,
    *,
    size_half_points: int = 24,
    bold: bool = False,
    italic: bool = False,
    center: bool = False,
    before: int = 0,
    after: int = 120,
    line_spacing: int = 360,
) -> str:
    return (
        "<w:p>"
        f"{ppr(line_spacing=line_spacing, before=before, after=after, center=center)}"
        "<w:r>"
        f"{rpr(size_half_points=size_half_points, bold=bold, italic=italic)}"
        f'<w:t xml:space="preserve">{escape(text)}</w:t>'
        "</w:r>"
        "</w:p>"
    )


def blank_paragraph() -> str:
    return paragraph("", after=0)


def page_break() -> str:
    return "<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>"


def build_document_xml() -> str:
    body_parts: list[str] = []

    for index, item in enumerate(REPORT_STRUCTURE):
        if item["type"] == "title_page":
            body_parts.append(paragraph(item["title"], size_half_points=40, bold=True, center=True, before=800, after=200))
            body_parts.append(paragraph(item["subtitle"], size_half_points=32, bold=True, center=True, after=400))
            for line in item["details"]:
                body_parts.append(paragraph(line, size_half_points=24, center=True, after=180))
        elif item["type"] == "toc":
            body_parts.append(paragraph(item["title"], size_half_points=36, bold=True, center=True, after=300))
            for i, entry in enumerate(item["entries"], start=1):
                body_parts.append(paragraph(f"{i}. {entry}", size_half_points=24, after=140))
        else:
            body_parts.append(paragraph(item["title"], size_half_points=36, bold=True, after=220))
            for section in item["sections"]:
                body_parts.append(paragraph(section["heading"], size_half_points=28, bold=True, after=160))
                for para in section["paragraphs"]:
                    body_parts.append(paragraph(para, size_half_points=24, after=130))
                body_parts.append(blank_paragraph())
        if index < len(REPORT_STRUCTURE) - 1:
            body_parts.append(page_break())

    sect = (
        "<w:sectPr>"
        "<w:pgSz w:w=\"11906\" w:h=\"16838\"/>"
        "<w:pgMar w:top=\"1440\" w:right=\"1440\" w:bottom=\"1440\" w:left=\"1440\" "
        "w:header=\"708\" w:footer=\"708\" w:gutter=\"0\"/>"
        "</w:sectPr>"
    )

    body = "".join(body_parts) + sect
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:document xmlns:wpc=\"http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas\" "
        "xmlns:mc=\"http://schemas.openxmlformats.org/markup-compatibility/2006\" "
        "xmlns:o=\"urn:schemas-microsoft-com:office:office\" "
        "xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" "
        "xmlns:m=\"http://schemas.openxmlformats.org/officeDocument/2006/math\" "
        "xmlns:v=\"urn:schemas-microsoft-com:vml\" "
        "xmlns:wp14=\"http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing\" "
        "xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\" "
        "xmlns:w10=\"urn:schemas-microsoft-com:office:word\" "
        "xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" "
        "xmlns:w14=\"http://schemas.microsoft.com/office/word/2010/wordml\" "
        "xmlns:wpg=\"http://schemas.microsoft.com/office/word/2010/wordprocessingGroup\" "
        "xmlns:wpi=\"http://schemas.microsoft.com/office/word/2010/wordprocessingInk\" "
        "xmlns:wne=\"http://schemas.microsoft.com/office/word/2006/wordml\" "
        "xmlns:wps=\"http://schemas.microsoft.com/office/word/2010/wordprocessingShape\" "
        "mc:Ignorable=\"w14 wp14\">"
        f"<w:body>{body}</w:body>"
        "</w:document>"
    )


CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""


ROOT_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""


DOC_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>
"""


CORE_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:dcterms="http://purl.org/dc/terms/"
 xmlns:dcmitype="http://purl.org/dc/dcmitype/"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>AI Music Generator Detailed Project Report</dc:title>
  <dc:subject>AI Music Generator</dc:subject>
  <dc:creator>Codex</dc:creator>
  <cp:keywords>AI, Music Generator, Flask, NumPy, SciPy, Report</cp:keywords>
  <dc:description>Detailed Word report for the AI Music Generator project.</dc:description>
</cp:coreProperties>
"""


APP_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
 xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office Word</Application>
</Properties>
"""


def main() -> None:
    document_xml = build_document_xml()
    with ZipFile(OUTPUT, "w", compression=ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", CONTENT_TYPES_XML)
        zf.writestr("_rels/.rels", ROOT_RELS_XML)
        zf.writestr("word/document.xml", document_xml)
        zf.writestr("word/_rels/document.xml.rels", DOC_RELS_XML)
        zf.writestr("docProps/core.xml", CORE_XML)
        zf.writestr("docProps/app.xml", APP_XML)
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()
