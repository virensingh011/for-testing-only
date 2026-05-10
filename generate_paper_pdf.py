from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors


def build_pdf():
    doc = SimpleDocTemplate("technical-paper.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Aegis Atlas Technical Paper", styles["Title"]))
    story.append(Paragraph("Graph-Based Risk Routing and Flow Capacity in a Browser Simulation", styles["Heading2"]))
    story.append(Paragraph("Author: Viren Singh", styles["Normal"]))
    story.append(Spacer(1, 14))

    sections = [
        ("Problem", "Aegis Atlas explores how risk can move across a connected regional network. Nodes represent cities, hospitals, industrial centers, or infrastructure hubs. Edges represent transport, communication, or dependency links. The technical problem is to estimate risk propagation, find a shortest emergency route, and calculate maximum flow capacity between a source and a sink."),
        ("Algorithms: Dijkstra + Edmonds-Karp", "Dijkstra's algorithm computes a shortest path on a graph with non-negative weights. In this implementation, edge reliability is converted into route cost using cost = 1 / weight. Edmonds-Karp computes maximum flow by repeatedly finding breadth-first augmenting paths in a residual graph. The propagation model is R_i(t+1) = alpha H_i + beta E_i + gamma N_i(t) + delta C_i - lambda P_i."),
        ("Your Implementation", "The browser implementation contains a weighted graph of six infrastructure nodes and seven edges. Dijkstra is used for route planning from Coast City to Medical Center. Edmonds-Karp estimates maximum flow capacity across the same graph. The simulation also supports time-step playback, scenario comparison, and Monte Carlo uncertainty runs."),
    ]

    for title, body in sections:
        story.append(Paragraph(title, styles["Heading1"]))
        story.append(Paragraph(body, styles["BodyText"]))
        story.append(Spacer(1, 10))

    story.append(Paragraph("Results Table", styles["Heading1"]))
    table = Table([
        ["Metric", "Result"],
        ["Dijkstra source/sink", "Coast City to Medical Center"],
        ["Max-flow source/sink", "Coast City to Medical Center"],
        ["Unit tests", "Path existence, finite distance, positive flow, augmenting edges"],
        ["Benchmark", "Browser Performance API repeated trials"],
        ["Monte Carlo", "160 uncertainty trials"],
    ], colWidths=[170, 330])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dbeafe")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 7),
    ]))
    story.append(table)
    story.append(Spacer(1, 12))

    story.append(Paragraph("Limitations", styles["Heading1"]))
    story.append(Paragraph("The graph is intentionally small so the project can run on static hosting. Public API requests may be blocked when opened from local files. The model uses simplified weights and should be treated as an educational computational model, not as an operational emergency management tool.", styles["BodyText"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("References", styles["Heading1"]))
    story.append(Paragraph("Dijkstra, E. W. (1959). A note on two problems in connexion with graphs. Numerische Mathematik, 1, 269-271. https://doi.org/10.1007/BF01386390", styles["BodyText"]))
    story.append(Paragraph("Edmonds, J., & Karp, R. M. (1972). Theoretical improvements in algorithmic efficiency for network flow problems. Journal of the ACM, 19(2), 248-264. https://doi.org/10.1145/321694.321699", styles["BodyText"]))

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
