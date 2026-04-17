GRC Master Dashboard
A comprehensive Governance, Risk, and Compliance (GRC) dashboard designed to provide real-time monitoring and insights for organizational security posture, compliance status, and risk management.

GRC Dashboard License HTML5 Bootstrap Chart.js

📋 Table of Contents
Features
Demo
Installation
Usage
Technical Stack
Project Structure
Configuration
API Integration
Contributing
License
Contact
✨ Features
Executive Summary Cards: Real-time visualization of key GRC metrics
Open Risks count
Active Incidents tracking
Compliance percentage (ISO 27001)
Governance Alerts monitoring
Interactive Charts:
Risk Analysis Heatmap (Bar Chart)
DPDP Consent Status (Doughnut Chart)
Data Tables:
Data Flow Map (Phase 13)
Vendor Risks Assessment (Phase 7)
Modern UI/UX:
Dark theme with glassmorphism effects
Responsive design for all screen sizes
Smooth animations and transitions
Professional color scheme and typography
Auto-refresh: Dashboard automatically refreshes every 10 seconds to show latest data
🚀 Demo
The dashboard provides a comprehensive view of your organization's GRC posture:

Dashboard Preview

📦 Installation
Prerequisites
A modern web browser (Chrome, Firefox, Safari, Edge)
A local web server (optional, but recommended)
Basic knowledge of HTML/CSS/JavaScript
Steps
Clone the repository:
bash

git clone https://github.com/yourusername/grc-master-dashboard.git
Navigate to the project directory:
bash

cd grc-master-dashboard
Open the index.html file in your web browser or serve it using a local web server:
bash

# Using Python 3
python -m http.server 8000

# Using Node.js (with http-server installed)
npx http-server
Access the dashboard at http://localhost:8000 (or the port specified by your server).
🔧 Usage
First Time Setup
API Configuration: The dashboard is designed to work with a backend API. Update the API endpoints in the JavaScript section of index.html:
javascript

// Example API endpoints (update these according to your backend)
const API_ENDPOINTS = {
    incidents: '/api/incidents/stats',
    alerts: '/api/governance/alerts',
    compliance: '/api/compliance/stats',
    risks: '/api/risks',
    consents: '/api/dpdp/consents',
    vendors: '/api/vendors',
    flows: '/api/dataflow/flows'
};
Mock Data Mode: If you don't have a backend API ready, the dashboard includes a mock data mode for demonstration purposes. The initDashboard() function will use mock data when API calls fail.
Dashboard Navigation
Executive Summary: View key metrics at a glance
Risk Analysis: Monitor risk distribution and severity
DPDP Compliance: Track consent status for data privacy
Data Flows & Vendors: Review data flow mappings and vendor risk assessments
Refreshing Data
The dashboard automatically refreshes every 10 seconds to display the latest data. You can also manually refresh by reloading the page.

🛠 Technical Stack
HTML5: Structure and content
CSS3: Styling and animations
Bootstrap 5.3: UI framework and responsive design
Chart.js: Data visualization
JavaScript (ES6+): Logic and interactivity
FontAwesome 6.4: Icons
📁 Project Structure
text

grc-master-dashboard/
├── index.html          # Main dashboard file
├── README.md           # This file
├── assets/             # Images, fonts, and other assets
│   ├── images/         # Dashboard screenshots and logos
│   ├── fonts/          # Custom fonts (if any)
│   └── icons/          # Custom icons (if any)
├── css/                # Custom CSS files (if any)
│   └── styles.css      # Additional styles
└── js/                 # Custom JavaScript files (if any)
    └── dashboard.js    # Dashboard logic (currently embedded in index.html)
⚙️ Configuration
Dashboard Settings
You can customize the dashboard by modifying the following sections in index.html:

Auto-refresh Interval: Change the refresh interval (currently set to 10000ms):
javascript

// Auto Refresh every 10 seconds
initDashboard();
setInterval(initDashboard, 10000); // Change 10000 to desired interval in milliseconds
Chart Colors: Modify the color scheme for charts:
javascript

// Risk Chart Colors
backgroundColor: ['#28a745', '#ffc107', '#fd7e14', '#dc3545'] 
// Green, Yellow, Orange, Red for Low, Medium, High, Critical

// DPDP Chart Colors
backgroundColor: ['#28a745', '#dc3545'] 
// Green for Active, Red for Revoked
Card Colors: Customize the executive summary cards:
🔌 API Integration
The dashboard expects the following API endpoints:

1. Incidents Stats
text

GET /api/incidents/stats
Response: { "total_open": 5 }
2. Governance Alerts
text

GET /api/governance/alerts
Response: [
  { "id": 1, "type": "Policy Violation", "severity": "High", "description": "..." },
  ...
]
3. Compliance Stats
text

GET /api/compliance/stats
Response: {
  "ISO 27001": { "percentage": 94 },
  "GDPR": { "percentage": 87 },
  ...
}
4. Risks
text

GET /api/risks
Response: [
  { "id": 1, "title": "Data Breach Risk", "level": "High", "owner": "IT Security" },
  ...
]
5. DPDP Consents
text

GET /api/dpdp/consents
Response: [
  { "id": 1, "user_id": "user123", "status": "Active", "date": "2023-01-01" },
  ...
]
6. Vendors
text

GET /api/vendors
Response: [
  { "id": 1, "name": "Cloud Services Inc.", "service": "Cloud Storage", "risk_score": 25 },
  ...
]
7. Data Flows
text

GET /api/dataflow/flows
Response: [
  { "id": 1, "source": "CRM System", "dest": "Analytics Engine", "type": "PII Transfer" },
  ...
]
🤝 Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository
Create a new branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request
Development Guidelines
Follow the existing code style
Add comments for complex logic
Test your changes thoroughly
Update the README if needed
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
If you have any questions, suggestions, or issues, please:

Open an issue on GitHub
Contact the project maintainer at your.email@example.com
🙏 Acknowledgments
Bootstrap team for the excellent UI framework
Chart.js team for the powerful charting library
FontAwesome for the icon set
