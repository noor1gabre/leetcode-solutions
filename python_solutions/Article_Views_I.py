import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Find authors who viewed their own articles
    result = views[views['author_id'] == views['viewer_id']]['author_id'].unique()

    # Convert result to a regular Python list
    result = list(result)

    # Sort the result
    result.sort()

    # Display the result
    return pd.DataFrame({'id': result})