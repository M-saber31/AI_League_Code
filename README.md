<p>Project Name: Real-Time Player Impact Analyzer (RTPIA)
Team Name اﻟﺴﺘﺪﻳﻮ اﻟﺘﺤﻠﻴﻠﻲ اﻟﻤﻤﺘﺎز
Team Members :Yousif Ahmed Mohamed Saber
Contents:Team Members01The Problem and Its Solution02All Data Used (Textual and Non-Textual)03Technologies Used04Idea Description05How These Data Are Provided and Utilized06Goal Alignment0708Demo and Testing09ChallengesThe Problem and its solution Problem: Coaches and analysts lack real-time insights into player contributions during soccer matches, relying on post-game stats that miss dynamic impact of players like who facilitate ball control and link attacks. Solution: Real-Time Player Impact Analyzer (RTPIA) uses a GNN to estimate ΔxT from live match events, enhanced by YOLO to detect players and the ball, delivering instant performance metrics. Innovation: Combines cutting-edge GNN with computer vision for live, actionable insights, empowering tactical decisions mid-game.Expected Threat (xT)Graph Neural Network (GNN)Used dataThis section explains all the data collected or generated during the project, whether textual (e.g., texts) or non-textual (e.g., images and graphs)- Generated: Real-time events with ΔxT predictions, linking detected players to actions.- Textual: 1) Wyscout match event data (e.g., passes, tackles) for training GNN on Δ xT.2) Sofascore player stats dataset throughout the whole season -Non- Textual: 1 ) Live video feeds from matches, processed by YOLO to detect players (bounding boxes) and ball positions.2) Roboflow football match bounding box data for different classes such football players Technologies Used- Python: Programming Language - YOLOv8: Real-time player and ball detection from video streams.- PyTorch &amp; PyTorch Geometric: GNN (GoalNet) for ΔxT prediction.- Hardware: GPU (e.g., NVIDIA Tesla 4) for real-time computation in google colab.Value: Solves delayed analysis by delivering live insights; targets coaches needing instant metrics. Market: Soccer clubs, analysts; growing sports tech sector ($30B by 2026). - Process: Live video → YOLO detects players/ball → Maps to event data → GNN predicts ΔxT per player. - Benefits: Instant tactical feedback, identifies hidden contributors (e.g., defensive pivots). - Innovation: First system merging GNN-based ΔxT with live vision, unlike static post-game tools.Real-Time Player Impact Analyzer (RTPIA)Idea descriptionHow the Data Is Provided and UtilizedPlayer-Specific Data: Which are the statistics of the players throughout the season and those are provided by scraping the statistics API in the Sofascore WebsiteEvent Data: This data is provided from the Wyscout public dataset and we convert it into SPADL format so that it would be ready to be used to create edges between the players and calculate the ΔxT for each event Football-Players-DetectionAnnotation dataset : Labeled , Football players, ball refrees, and goalkeepers provided from Roboflow platform to train YOLOv8 modelGoal Alignment:Goal Alignment - Theme: Improving Performance - Fit: Enhances player and team performance by providing live ΔxT insights, enabling mid-game adjustments to boost win rates.Testing/Validation: Demo/screenshots/Video/Simulations; ServerClientChallenges &amp; Future Work●Challenges: 1) How to detect different events throughout the match .2) How to make the experience more real-time ●What You Need Help With: Access to more computing units and better GPUs on google colab.●Future Works: Real-time event detection → Train GNN on collected data → GNN predicts ΔxT per player. Thank YouProject code: https://github.com/M-saber31/AI<em>League</em>Code</p>
