# Executive Advertisement Channel Analysis Report

**Date:** 2026-06-15
**Dataset:** 200 rows of advertising spend across TV, Radio, Newspaper channels and corresponding Sales.

## 1. Introduction
This report provides an analysis of advertising channel effectiveness based on a dataset of 200 observations. We examine the descriptive statistics of spend across TV, Radio, and Newspaper, and their correlation with product sales to identify key insights and provide strategic recommendations.

## 2. Descriptive Statistics Overview

| Metric    | TV         | Radio      | Newspaper  | Sales      |
|:----------|:-----------|:-----------|:-----------|:-----------|
| **Count** | 200.00     | 200.00     | 200.00     | 200.00     |
| **Mean**  | 147.04     | 23.26     | 30.55     | 14.02     |
| **Std Dev**| 85.85     | 14.85     | 21.78     | 5.22     |
| **Min**   | 0.70     | 0.00     | 0.30     | 1.60     |
| **25%**   | 74.38     | 9.97     | 12.75     | 10.38     |
| **50%**   | 149.75     | 22.90     | 25.75     | 12.90     |
| **75%**   | 218.82     | 36.52     | 45.10     | 17.40     |
| **Max**   | 296.40     | 49.60     | 114.00     | 27.00     |

**Key Observations from Descriptive Statistics:**
*   **TV:** Shows the highest average spend (147.04) and the widest range of spend (0.70 to 296.40), indicating significant investment variability.
*   **Radio:** Has a moderate average spend (23.26) with a range from 0.00 to 49.60. The minimum spend of 0.00 suggests some observations had no radio advertising.
*   **Newspaper:** Has an average spend of 30.55, but its maximum spend (114.00) is notably higher than its 75th percentile (45.10), suggesting potential outliers or a right-skewed distribution in newspaper advertising spend.
*   **Sales:** Average sales are 14.02, ranging from 1.60 to 27.00.

## 3. Correlation Analysis

The Pearson Correlation Matrix reveals the linear relationship between advertising channels and sales:

|           | TV       | Radio    | Newspaper| Sales    |
|:----------|:---------|:---------|:---------|:---------|
| **TV**    | 1.00     | 0.05     | 0.06     | **0.78** |
| **Radio** | 0.05     | 1.00     | 0.35     | **0.58** |
| **Newspaper**| 0.06     | 0.35     | 1.00     | **0.23** |
| **Sales** | **0.78** | **0.58** | **0.23** | 1.00     |

**Key Observations from Correlation Matrix:**
*   **TV and Sales (0.78):** There is a strong positive correlation between TV advertising spend and Sales. This suggests that increased investment in TV advertising is highly associated with an increase in sales.
*   **Radio and Sales (0.58):** A moderate positive correlation exists between Radio advertising spend and Sales. While not as strong as TV, Radio still shows a significant positive impact on sales.
*   **Newspaper and Sales (0.23):** The correlation between Newspaper advertising spend and Sales is weak. This indicates that Newspaper advertising has a much smaller linear relationship with sales compared to TV and Radio.
*   **Inter-channel Correlation:** The correlations between the advertising channels themselves (e.g., TV-Radio, TV-Newspaper) are very low (0.05-0.06), except for Radio-Newspaper (0.35). This low multicollinearity among channels is generally good for modeling, as it suggests each channel's effect can be more independently assessed.

## 4. Strategic Recommendations

Based on the analysis, the following recommendations are proposed:

1.  **Prioritize TV Advertising:** Given the strong positive correlation (0.78) with sales, TV advertising should be considered the primary channel for investment to drive sales growth. Further analysis could explore optimal TV spend levels.
2.  **Maintain or Optimize Radio Advertising:** Radio advertising shows a moderate positive correlation (0.58). It's a valuable channel, but its effectiveness is less pronounced than TV. Consider optimizing radio campaigns for target audience and timing to maximize ROI.
3.  **Re-evaluate Newspaper Advertising:** With a weak correlation (0.23) to sales, the effectiveness of Newspaper advertising is questionable. It is recommended to:
    *   Investigate if Newspaper advertising serves other strategic goals (e.g., brand awareness, local reach) not captured by sales figures alone.
    *   Consider reallocating budget from Newspaper to more effective channels like TV or Radio, or explore alternative digital channels if the goal is direct sales impact.
    *   If Newspaper advertising is retained, conduct A/B testing or more targeted experiments to understand its true impact and potential for improvement.
4.  **Further Analysis:** While this report focuses on linear correlations, a more advanced regression model could quantify the exact impact of each channel on sales, considering potential interactions between channels.

## 5. Conclusion
TV advertising is the most impactful channel for driving sales, followed by Radio. Newspaper advertising shows a significantly weaker relationship with sales. Strategic allocation of advertising budget should reflect these findings, prioritizing channels with higher demonstrated effectiveness.
