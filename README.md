<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
</head>
<body>

  <h1>✅ PROJECT 1 — Customer Analytics &amp; Prediction System</h1>
  <h2>(ML Fundamentals + API-Based Inference)</h2>

  <hr />

  <h2>📌 Project Overview</h2>
  <p>
    This project implements a <strong>Customer Analytics and Prediction System</strong> using
    <strong>core Machine Learning concepts only</strong>. The focus is on
    <strong>data preprocessing</strong>, <strong>classical ML algorithms</strong>,
    <strong>evaluation metrics</strong>, and <strong>API-based inference</strong>,
    without training heavy models locally.
  </p>
  <p>
    Machine learning predictions are obtained via <strong>external ML APIs</strong>,
    while all <strong>data handling, feature engineering, and evaluation logic</strong>
    is implemented within the project.
  </p>

  <hr />

  <h2>🎯 Learning Objectives (STRICT)</h2>
  <p>This project covers <strong>ONLY</strong> the following ML topics:</p>
  <ul>
    <li>Python (NumPy, Pandas, Matplotlib, Seaborn)</li>
    <li>Data Cleaning &amp; EDA</li>
    <li>Feature Scaling (StandardScaler)</li>
    <li>Feature Encoding (One-Hot Encoding)</li>
    <li>
      Supervised ML:
      <ul>
        <li>Linear Regression</li>
        <li>Logistic Regression</li>
        <li>Decision Tree</li>
        <li>Random Forest</li>
        <li>KNN</li>
      </ul>
    </li>
    <li>
      Unsupervised ML:
      <ul>
        <li>K-Means Clustering</li>
        <li>PCA</li>
      </ul>
    </li>
    <li>
      Model Evaluation:
      <ul>
        <li>Accuracy, Precision, Recall, F1-score, ROC-AUC</li>
        <li>Overfitting vs Underfitting</li>
        <li>Bias vs Variance</li>
      </ul>
    </li>
  </ul>
  <p><strong>❌ No other ML concepts are used.</strong></p>

  <hr />

  <h2>🧩 System Architecture</h2>
  <pre>
Client
   |
   v
FastAPI Application
   |
   |-- Data Cleaning
   |-- Feature Engineering
   |
   v
External ML Inference API
   |
   v
Prediction Response
  </pre>

  <hr />

  <h2>🛠 Tech Stack</h2>
  <ul>
    <li>Python</li>
    <li>FastAPI</li>
    <li>Pandas, NumPy</li>
    <li>Matplotlib, Seaborn</li>
    <li>Hugging Face Inference API</li>
    <li>Docker</li>
  </ul>

  <hr />

  <h2>🔹 PHASE 1 — Project Setup &amp; Dataset Understanding</h2>
  <h3>Goal</h3>
  <p>Understand the problem and dataset before applying ML.</p>
  <h3>Tasks</h3>
  <ul>
    <li>Create project repository</li>
    <li>Setup Python environment</li>
    <li>Load customer dataset</li>
    <li>
      Identify:
      <ul>
        <li>Target variable</li>
        <li>Input features</li>
      </ul>
    </li>
    <li>Define prediction goals (churn / purchase)</li>
  </ul>
  <h3>Concepts Used</h3>
  <ul>
    <li>Python basics</li>
    <li>Pandas DataFrames</li>
  </ul>

  <hr />

  <h2>🔹 PHASE 2 — Data Cleaning &amp; EDA</h2>
  <h3>Goal</h3>
  <p>Prepare clean, usable data.</p>
  <h3>Tasks</h3>
  <ul>
    <li>Handle missing values</li>
    <li>Detect and treat outliers</li>
    <li>
      Perform EDA:
      <ul>
        <li>Histograms</li>
        <li>Box plots</li>
        <li>Correlation heatmap</li>
      </ul>
    </li>
    <li>Identify data leakage risks</li>
  </ul>
  <h3>Concepts Used</h3>
  <ul>
    <li>Pandas</li>
    <li>Matplotlib / Seaborn</li>
    <li>Correlation analysis</li>
  </ul>

  <hr />

  <h2>🔹 PHASE 3 — Feature Engineering</h2>
  <h3>Goal</h3>
  <p>Transform raw data into ML-ready features.</p>
  <h3>Tasks</h3>
  <ul>
    <li>Apply One-Hot Encoding</li>
    <li>Apply StandardScaler</li>
    <li>Separate features and labels</li>
    <li>Prepare final feature matrix</li>
  </ul>
  <h3>Concepts Used</h3>
  <ul>
    <li>One-Hot Encoding</li>
    <li>Feature scaling</li>
    <li>Linear algebra intuition (weights)</li>
  </ul>

  <hr />

  <h2>🔹 PHASE 4 — ML Model Inference (API-Based)</h2>
  <h3>Goal</h3>
  <p>Use classical ML models via API for predictions.</p>
  <h3>Models Used (Conceptually)</h3>
  <ul>
    <li>Logistic Regression</li>
    <li>Decision Tree</li>
    <li>Random Forest</li>
    <li>KNN</li>
  </ul>
  <h3>Tasks</h3>
  <ul>
    <li>Send feature vectors to ML API</li>
    <li>Receive prediction outputs</li>
    <li>Store prediction results</li>
  </ul>
  <h3>Concepts Used</h3>
  <ul>
    <li>Supervised learning</li>
    <li>Classification logic</li>
  </ul>

  <hr />

  <h2>🔹 PHASE 5 — Model Evaluation</h2>
  <h3>Goal</h3>
  <p>Evaluate prediction quality using ML metrics.</p>
  <h3>Tasks</h3>
  <ul>
    <li>Train/Test split logic (conceptual)</li>
    <li>
      Compute:
      <ul>
        <li>Accuracy</li>
        <li>Precision</li>
        <li>Recall</li>
        <li>F1-score</li>
        <li>ROC-AUC</li>
      </ul>
    </li>
    <li>Analyze overfitting vs underfitting</li>
  </ul>
  <h3>Concepts Used</h3>
  <ul>
    <li>Classification metrics</li>
    <li>Bias vs variance</li>
  </ul>

  <hr />

  <h2>🔹 PHASE 6 — Customer Segmentation (Unsupervised ML)</h2>
  <h3>Goal</h3>
  <p>Group customers based on behavior.</p>
  <h3>Tasks</h3>
  <ul>
    <li>Apply K-Means clustering</li>
    <li>Use PCA for visualization</li>
    <li>Analyze clusters</li>
  </ul>
  <h3>Concepts Used</h3>
  <ul>
    <li>K-Means</li>
    <li>PCA</li>
  </ul>

  <hr />

  <h2>🔹 PHASE 7 — API Development</h2>
  <h3>Goal</h3>
  <p>Expose ML predictions via REST API.</p>
  <h3>Endpoints</h3>
  <ul>
    <li><code>/predict/churn</code></li>
    <li><code>/predict/purchase</code></li>
    <li><code>/cluster/customers</code></li>
  </ul>
  <h3>Concepts Used</h3>
  <ul>
    <li>API-based ML inference</li>
    <li>Input validation</li>
  </ul>

  <hr />

  <h2>🔹 PHASE 8 — Documentation &amp; Finalization</h2>
  <h3>Goal</h3>
  <p>Prepare project for interviews.</p>
  <h3>Tasks</h3>
  <ul>
    <li>Write README</li>
    <li>Add results summary</li>
    <li>Add sample API requests</li>
  </ul>

</body>
</html>
