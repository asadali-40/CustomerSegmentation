# Customer Segmentation Using K-Means Clustering

Developed an end-to-end Machine Learning project to segment customers into distinct groups based on purchasing behavior and demographic characteristics. The project leverages the K-Means Clustering algorithm, an unsupervised machine learning technique, to identify meaningful customer segments using Age, Annual Income, and Spending Score data.

The workflow began with data preprocessing, including handling missing values, data cleaning, exploratory data analysis (EDA), and feature scaling using StandardScaler to ensure all variables contributed equally to the clustering process. The optimal number of clusters was determined through the Elbow Method and Silhouette Score analysis, resulting in four distinct customer segments.

After training the K-Means model, customer groups were analyzed and assigned business-friendly labels based on their spending patterns and income levels. These segments provide valuable insights that can help businesses improve targeted marketing campaigns, customer retention strategies, and personalized promotions.

To make the solution interactive and user-friendly, a Streamlit web application was developed. The application allows users to input customer information such as age, annual income, and spending score, and instantly predicts the corresponding customer segment using the trained clustering model. The prediction pipeline includes automated data preprocessing, feature scaling, cluster prediction, and segment mapping.

The project demonstrates practical applications of unsupervised machine learning in customer analytics while showcasing skills in data preprocessing, clustering, model evaluation, feature engineering, model deployment, and web application development.

### Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* K-Means Clustering
* StandardScaler
* Matplotlib
* Streamlit

### Key Features

* Customer segmentation using unsupervised learning
* Data preprocessing and feature scaling
* Optimal cluster selection using evaluation metrics
* Real-time customer segment prediction
* Interactive Streamlit dashboard
* Business-oriented customer profiling and insights

