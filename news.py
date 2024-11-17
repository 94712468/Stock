import tkinter as tk
import random

stock_impacts = {
    5: [
        "Major new product line launches successful, exceeding sales projections.",
        "Expansion into e-commerce leads to record online sales.",
        "Strategic acquisition expands product line and market presence.",
        "New health trend drives demand for gourmet olives.",
        "Successful community engagement initiatives boost brand loyalty."
    ],
    4: [
        "Strong Q3 earnings report leads to increased analyst ratings.",
        "Positive industry awards boost brand credibility.",
        "New flavor line gains popularity, driving sales up.",
        "High-profile sponsorship increases brand awareness.",
        "Record-setting earnings report surprises analysts positively.",
        "New export agreement boosts international sales significantly.",
        "Major retail chain features Olves in a national campaign.",
        "Increased market share reported in the domestic market."
    ],
    3: [
        "Successful expansion into a new geographic region.",
        "Attendance at a major trade show leads to new partnerships.",
        "Enhanced sustainability initiatives resonate with consumers.",
        "Consumer loyalty program shows positive early results.",
        "Positive consumer reviews drive higher demand.",
        "New flavors introduced receive positive customer feedback.",
        "Analysts upgrade stock based on solid fundamentals.",
        "Key product featured in a popular food magazine.",
        "Sales forecast revised upward after strong quarterly performance."
    ],
    2: [
        "Positive earnings revisions from analysts after strong sales data.",
        "Moderate increase in market demand during the holiday season.",
        "Steady growth in online sales channel.",
        "Stable profit margins support steady growth outlook.",
        "Incremental sales growth observed in established markets.",
        "Strong sales growth reported in seasonal product lines.",
        "New distribution deals announced, expanding market reach.",
        "Positive feedback from a recent advertising campaign."
    ],
    1: [
        "Olves gets visited by international food taster, results await."
        "Ongoing projects show promise, keeping investor interest alive.",
        "Brand remains stable amid market challenges.",
        "Consistent dividend payouts maintain investor interest.",
        "Incremental growth in share price reflects steady performance.",
        "Mild increase in sales due to seasonal trends.",
        "Small uptick in customer engagement metrics."
    ],
    0: [
        "Quarterly earnings meet expectations but no surprises.",
        "Market stability leads to little movement in stock price.",
        "Earnings report shows no major changes from last quarter.",
        "Company maintains steady performance amid external factors.",
        "New marketing strategy implemented, showing neutral impact.",
        "Stock price remains stable despite broader market fluctuations."
    ],
    -1: [
        "Minor sales drop in a competitive quarter.",
        "Slight decline in sales due to increased competition.",
        "Small reduction in forecast due to unexpected costs.",
        "Increased operational costs lead to lower profit margins.",
        "Minor adjustments made to production schedules.",
        "Slight drop in consumer satisfaction scores."
    ],
    -2: [
        "Olves attempts to market in a new country."
        "Increased competition results in price wars.",
        "Temporary supply shortages impact sales performance.",
        "Unfavorable regulatory changes increase operating costs.",
        "Shifts in consumer preferences lead to lower olive sales.",
        "Sales from a key market dip slightly.",
        "Initial consumer response to a new product is lukewarm."
    ],
    -3: [
        "Legal challenges result in costly settlements.",
        "Poor quarterly projections lead to reduced investor confidence.",
        "Negative feedback from a focus group impacts product launches.",
        "Rising raw material costs squeeze profit margins.",
        "Negative media coverage affects brand perception.",
        "Minor product recall causes short-term stock decline."
    ],
    -4: [
        "Declining sales in key markets trigger investor concerns.",
        "Reports of food safety issues lead to consumer backlash.",
        "Economic indicators suggest consumer spending may decline.",
        "Product pricing issues cause concern among investors.",
        "Slowdown in growth of the gourmet food sector raises alarms.",
        "Loss of a key distributor disrupts sales channels.",
        "Internal audit reveals discrepancies in financial reporting."
    ],
    -5: [
        "Major product line fails to meet consumer expectations, resulting in a recall.",
        "Significant financial loss reported due to market exit.",
        "Comprehensive audit reveals financial mismanagement issues.",
        "Major management shake-up results in loss of investor trust.",
        "Lawsuit settlement results in significant financial loss.",
        "Major supplier bankruptcy disrupts operations significantly.",
        "Significant layoffs announced, raising red flags for investors.",
        "Major cybersecurity breach leads to significant reputational damage."
    ]
}



class NewsWidget:
    def __init__(self, window):
        self.current_impact = 0
        self.previous_impact = 0
        self.current_news = ""
        self.text = tk.StringVar(value = self.current_news)
        self.news = tk.Label(
            window, 
            textvariable=self.text)
        self.news.grid(row=9, column=1)

        self.randomize_news()

        # self.counter = 0

    def update(self):
        self.randomize_news()
        # self.counter+=1

    def randomize_news(self):
        self.previous_impact = self.current_impact
        self.current_impact = random.randint(-5, 5)
        self.current_news = random.choice(stock_impacts[self.current_impact])
        self.text.set(self.current_news)
        
