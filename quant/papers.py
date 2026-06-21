def search_momentum_papers(query: str) -> list[dict]:
    papers = [
        {
            "title": "Returns to Buying Winners and Selling Losers",
            "citation": "Jegadeesh and Titman (1993)",
            "summary": "This classic paper documents intermediate-horizon momentum in US equities. It motivates ranking stocks by prior returns and holding recent winners while controlling implementation assumptions.",
        },
        {
            "title": "Fact, Fiction, and Momentum Investing",
            "citation": "Asness, Frazzini, Israel, and Moskowitz (2014)",
            "summary": "The authors review common objections to momentum and argue that momentum is persistent across markets, but requires attention to crashes, turnover, and portfolio construction.",
        },
        {
            "title": "Momentum Crashes",
            "citation": "Daniel and Moskowitz (2016)",
            "summary": "This work highlights that momentum can experience sharp reversals, especially after market stress. It is useful for the risk section of the research report.",
        },
    ]
    if "momentum" not in query.lower():
        papers.append(
            {
                "title": "Cross-Section of Expected Stock Returns",
                "citation": "Fama and French (1992)",
                "summary": "A broader factor-investing reference useful when comparing momentum with value, size, and quality factors.",
            }
        )
    return papers
