import plotly.graph_objects as go
import numpy as np

N = 1000
x = np.array([0, 16, 22, 26, 30, 32, 37, 42, 45, 49, 51,
             59, 66, 69, 76, 78, 85, 94, 101, 103, 105])
y = np.array([0, 0, 14, 22, 13, 13, 23, 31, 25, 25, 21,
              34, 42, 37, 37, 34, 42, 47, 27, 14, 0])
x_interp = np.linspace(x.min(), x.max(), N)
# interp() to interpolate y values
y_interp = np.interp(x_interp, x, y)
# Create figure
fig = go.Figure(
    data=[
        go.Scatter(
            x=x_interp, y=y_interp, mode="lines", line=dict(width=2, color="#77e83a")
        ),
        go.Scatter(
            x=x_interp, y=y_interp, mode="lines", line=dict(width=2, color="#3a7de8")
        ),
    ],
    layout=go.Layout(
        xaxis=dict(
            title="Time (s)", range=[-5, 120], autorange=False, zeroline=False),
        yaxis=dict(
            title="Speed (Km/h)", range=[-5, 50], autorange=False, zeroline=False),
        title_text="Operating Cycle",
        hovermode="closest",
        annotations=[dict(x=x[k], y=y[k], text=str(y[k]), font_size=10, showarrow=False, bgcolor='white')
                     for k in range(y.size)],
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(
                        label="Start",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {"duration": 105, "redraw": False, "easing": "linear"},
                            },
                        ],
                    )
                ],
            )
        ],
    ),
    frames=[
        go.Frame(
            data=[
                go.Scatter(
                    x=[x_interp[k]],
                    y=[y_interp[k]],
                    mode="markers",
                    marker=dict(color="#e83a3a", size=10),
                )
            ],
            layout=go.Layout(annotations=[dict(x=x_interp[k], y=y_interp[k], text="<b>"+str(
                round(y_interp[k], 2))+"</b>"+" km/h", font_size=20, showarrow=True, bgcolor='white', bordercolor='black')])
        )
        for k in range(N)
    ],
)
fig.show()
# fig.write_html("motor-operating-cycle.html")