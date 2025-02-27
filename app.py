import os
from flask import Flask, render_template_string
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

@app.route("/")
def index():
    # Create a Plotly chart
    data = [
        go.Bar(
            x=["Category A", "Category B", "Category C"],
            y=[10, 20, 30],
            name="Example Data",
        )
    ]
    layout = go.Layout(
        title="Example Plotly Chart",
        xaxis=dict(title="Categories"),
        yaxis=dict(title="Values"),
    )
    fig = go.Figure(data=data, layout=layout)
    
    # Convert the Plotly figure to HTML
    chart_html = pio.to_html(fig, full_html=False)
    
    # Return the HTML page with the embedded chart
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Plotly Flask Example</title>
    </head>
    <body>
        <h1>Plotly Chart Example with Flask</h1>
        <div>{{ chart | safe }}</div>
    </body>
    </html>
    """, chart=chart_html)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use Azure's assigned port
    app.run(host="0.0.0.0", port=port)
