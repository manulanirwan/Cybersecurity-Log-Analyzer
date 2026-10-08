from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
import io

class PDFReportGenerator:
    @staticmethod
    def create_report(analysis_data: dict) -> io.BytesIO:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=36
        )

        styles = getSampleStyleSheet()
        story = []

        title_style = ParagraphStyle(
            'ReportTitle',
            parent=styles['Heading1'],
            fontSize=22,
            textColor=colors.HexColor('#1E293B'),
            spaceAfter=12
        )
        story.append(Paragraph("Cybersecurity Threat Analysis Advisory", title_style))
        story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceAfter=15))

        severity = analysis_data.get("severity", "Unknown")
        sev_color = {
            "Critical": colors.HexColor('#DC2626'),
            "High": colors.HexColor('#EA580C'),
            "Medium": colors.HexColor('#D97706'),
            "Low": colors.HexColor('#2563EB')
        }.get(severity, colors.HexColor('#4B5563'))

        meta_data = [
            [Paragraph("<b>Primary Threat:</b>", styles['Normal']), Paragraph(analysis_data.get("primary_threat", "N/A"), styles['Normal'])],
            [Paragraph("<b>Severity:</b>", styles['Normal']), Paragraph(f"<font color='{sev_color.hexval()}'><b>{severity}</b></font>", styles['Normal'])],
            [Paragraph("<b>MITRE ATT&CK:</b>", styles['Normal']), Paragraph(analysis_data.get("mitre_attack_id", "N/A"), styles['Normal'])]
        ]

        t = Table(meta_data, colWidths=[120, 420])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
            ('PADDING', (0, 0), (-1, -1), 8),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(t)
        story.append(Spacer(1, 15))

        def add_section(heading, text_or_list):
            story.append(Paragraph(f"<b>{heading}</b>", styles['Heading3']))
            story.append(Spacer(1, 4))
            if isinstance(text_or_list, list):
                for item in text_or_list:
                    story.append(Paragraph(f"• {item}", styles['Normal']))
            else:
                story.append(Paragraph(str(text_or_list), styles['Normal']))
            story.append(Spacer(1, 12))

        add_section("1. Threat Summary", analysis_data.get("summary", ""))
        add_section("2. Why This is Suspicious", analysis_data.get("suspicion_reason", ""))
        add_section("3. Key Indicators of Compromise (IOCs)", analysis_data.get("indicators_of_compromise", []))
        add_section("4. Recommended Defensive Actions", analysis_data.get("recommended_actions", []))

        doc.build(story)
        buffer.seek(0)
        return buffer
