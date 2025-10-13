import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
st.markdown("""<h2>LSTM Hyperparameters:</h2>
<ul><li>
latent_options: Number of "hidden" units (neurons) in the LSTM layers. Higher values let the model capture more complex sequences, but can increase the risk of overfitting if data is limited.
            <br>latent_options = [32, 64, 128]
            </li>
<li>batch_options: Size of batches during training (how many samples processed before updating weights). Smaller sizes can make training noisier but help regularize, larger sizes speed up training but may smooth out too much detail.
            <br>batch_options = [16, 32, 64]
            </li>
<li>lr_options (learning rate): Controls how much model weights are adjusted during each update. Lower rates are safer but slower, higher rates train faster but may miss subtle patterns or overshoot optimal values.
            <br>lr_options = [0.001, 0.005, 0.01]
            </li></ul>        
""",unsafe_allow_html=True)
st.image("pages/lstm.png")

# Create figure
#fig = go.Figure()

# Define positions for boxes
#boxes = [
#    {"name": "Data", "x": 0.5, "y": 0.9, "width": 0.15, "height": 0.08},
#    {"name": "Row & Col<br>Sample", "x": 0.2, "y": 0.7, "width": 0.12, "height": 0.08},
#    {"name": "Row & Col<br>Sample", "x": 0.5, "y": 0.7, "width": 0.12, "height": 0.08},
#    {"name": "Row & Col<br>Sample", "x": 0.8, "y": 0.7, "width": 0.12, "height": 0.08},
#    {"name": "Tree 1", "x": 0.2, "y": 0.5, "width": 0.12, "height": 0.08},
#    {"name": "Tree 2", "x": 0.5, "y": 0.5, "width": 0.12, "height": 0.08},
#    {"name": "Tree 3", "x": 0.8, "y": 0.5, "width": 0.12, "height": 0.08},
#    {"name": "Combine", "x": 0.5, "y": 0.3, "width": 0.12, "height": 0.08},
#    {"name": "Final Pred", "x": 0.5, "y": 0.1, "width": 0.12, "height": 0.08}
#]

# Colors from the brand palette
#colors = ["#1FB8CD", "#DB4545", "#2E8B57", "#5D878F", "#D2BA4C"]

# Add boxes
#for i, box in enumerate(boxes):
#    color = colors[i % len(colors)]
    
#    fig.add_shape(
#        type="rect",
#        x0=box["x"] - box["width"]/2,
#        y0=box["y"] - box["height"]/2,
#        x1=box["x"] + box["width"]/2,
#        y1=box["y"] + box["height"]/2,
#        fillcolor=color,
#        line=dict(color="black", width=1)
#    )
    
#    fig.add_annotation(
#        x=box["x"],
#        y=box["y"],
#        text=box["name"],
#        showarrow=False,
#        font=dict(color="white", size=12, family="Arial Black"),
#        xanchor="center",
#        yanchor="middle"
#    )

# Add arrows
#arrows = [
    # Data to sampling
#    {"x0": 0.425, "y0": 0.86, "x1": 0.2, "y1": 0.74},
#    {"x0": 0.5, "y0": 0.86, "x1": 0.5, "y1": 0.74},
#    {"x0": 0.575, "y0": 0.86, "x1": 0.8, "y1": 0.74},
    # Sampling to trees
#    {"x0": 0.2, "y0": 0.66, "x1": 0.2, "y1": 0.54},
#    {"x0": 0.5, "y0": 0.66, "x1": 0.5, "y1": 0.54},
#    {"x0": 0.8, "y0": 0.66, "x1": 0.8, "y1": 0.54},
    # Trees to combine
#    {"x0": 0.2, "y0": 0.46, "x1": 0.44, "y1": 0.34},
#    {"x0": 0.5, "y0": 0.46, "x1": 0.5, "y1": 0.34},
#    {"x0": 0.8, "y0": 0.46, "x1": 0.56, "y1": 0.34},
    # Combine to final
#    {"x0": 0.5, "y0": 0.26, "x1": 0.5, "y1": 0.14}
#]

#for arrow in arrows:
#    fig.add_annotation(
#        x=arrow["x1"],
#        y=arrow["y1"],
#        ax=arrow["x0"],
#        ay=arrow["y0"],
#        xref="x",
#        yref="y",
#        axref="x",
#        ayref="y",
#        showarrow=True,
#        arrowhead=2,
#        arrowsize=1,
#        arrowwidth=2,
#        arrowcolor="black"
#    )

# Update layout
#fig.update_layout(
##    title="XGBoost Subsample & Feature Sampling",
#    xaxis=dict(range=[0, 1], showgrid=False, showticklabels=False, zeroline=False),
#    yaxis=dict(range=[0, 1], showgrid=False, showticklabels=False, zeroline=False),
#    showlegend=False,
#    plot_bgcolor="white"
#)

## Save as PNG and SVG
#fig.write_image("xgboost_sampling.png")
#fig.write_image("xgboost_sampling.svg", format="svg")

#print("Chart saved successfully")
st.markdown("""<h2>XGBoost Hyperparameters:</h2>

<ul><li>n_estimators: Number of trees (boosting rounds). More trees can improve fit but may cause overfitting or longer runtime.
            <br>n_estimators_options = [100, 300, 500]
            </li>
<li>max_depth: Maximum depth for each tree. Deeper trees capture complex patterns, but too much depth may cause overfitting.
            <br>max_depth_options = [4, 6, 8]
            </li>
<li>lr (learning rate): Step size for updating weights after each tree. Lower values mean slower learning, but can result in better generalization if more trees are added.
            <br>lr_options = [0.01, 0.05, 0.1]
            </li>
<li>subsample: Fraction of training data sampled for each tree. Values below 1.0 can help the model generalize and reduce overfitting.
            <br>subsample_options = [0.7, 0.8, 1.0]
            </li>
<li>colsample: Fraction of features randomly chosen per tree. Like subsample, it introduces variety to reduce overfitting and improve robustness.
            <br>colsample_options = [0.7, 0.8, 1.0]
</li></ul>
""",unsafe_allow_html=True)
st.image("pages/xgboost_sampling.png")
st.write("Subsample and colsample let XGBoost bring bagging’s randomness—which is good for generalization—into boosting, which is great for learning complex patterns. This makes the model more robust and less prone to overfitting.")