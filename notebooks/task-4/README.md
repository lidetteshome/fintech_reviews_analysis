# Task 4: Insights & Visualizations

This task brings everything together by surfacing actionable insights using visual analytics and review themes.

---

## Objectives

- Identify **drivers of satisfaction** and **pain points**
- Compare banks by sentiment & themes
- Recommend improvements
- Visualize results clearly

---

## Visuals Generated

- Sentiment distribution by bank
- Rating histograms
- Word clouds by theme

All saved to `outputs/`.

---

## Insights Example

```json
{
  "CBE": {
    "drivers": ["app", "i", "good"], 
    "pain_points": ["app", "i", "of"]
  },
  "BOA": {
    "drivers": ["app", "i", "good"], 
    "pain_points": ["app", "i", "a"]
  },
  "Dashen": {
    "drivers": ["app", "a", "dashen"],
    "pain_points": ["not", "app", "you"]
  }
}