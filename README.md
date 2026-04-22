# Crypto Screener

## Project Documentation

### Features
- Real-time cryptocurrency data.
- Charting and analysis tools.
- Customizable alerts based on market conditions.
- User-friendly interface.

### Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Shmel999/crypto-screener.git
   ```
2. Navigate to the project directory:
   ```bash
   cd crypto-screener
   ```
3. Install the dependencies:
   ```bash
   npm install
   ```

### Command List
- `npm start`: Starts the application in development mode.
- `npm run build`: Builds the application for production.
- `npm test`: Runs the test suite.

### Deployment Guide
To deploy the application:
1. Ensure that all production dependencies are installed.
2. Build the application using `npm run build`.
3. Deploy the contents of the `build` directory to your web server.

### Project Structure
```
crypto-screener/
├── src/
│   ├── components/    # React components
│   ├── services/      # API services
│   └── utils/         # Utility functions
├── public/            # Static files
├── package.json       # Project metadata and dependencies
└── README.md          # Project documentation
```