# COVID-19 Data Tracker Software

COVID-19 Data Tracker Software is a Python-based application that scrapes real-time COVID-19 statistics from Worldometers and displays both global and country-specific data using a Tkinter GUI. The app also sends desktop notifications with the latest COVID-19 reports.

## Features

- **Data Scraping:**  
  Retrieves current COVID-19 data (total cases, deaths, recoveries) from [Worldometers](https://www.worldometers.info/coronavirus/).

- **Global & Country Data:**  
  Displays worldwide statistics and allows users to enter a country name to fetch specific COVID-19 data.

- **Graphical User Interface (GUI):**  
  Built with Tkinter, the interface features a banner, data labels, and input fields for an interactive experience.

- **Desktop Notifications:**  
  Uses Plyer to send notifications, alerting users with updated COVID-19 reports.

- **Data Refresh:**  
  Includes a refresh function to update and reload data on demand.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies:**

   Install required packages via pip:

   ```bash
   pip install requests bs4 plyer
   ```

   *Note: Tkinter is included with Python on most systems.*

3. **Asset Setup:**

   Ensure that the asset files (such as the notification icon and banner image) are located at the paths specified in the code. Adjust the paths in the script if needed.

## Usage

Run the application from your command prompt or terminal:

```bash
python "COVID 19 DATA TRACKER SOFTWARE.py"
```

The GUI will launch, displaying global COVID-19 statistics. To get country-specific data, enter the country name in the input field and click the **find info** button. The application will also display desktop notifications with COVID-19 updates.

## Code Overview

- **Web Scraping:**  
  Uses `requests` to fetch HTML and `BeautifulSoup` to parse COVID-19 data.

- **GUI:**  
  Tkinter is used to create the user interface, displaying data and providing interactive buttons.

- **Notifications:**  
  The `plyer.notification` module sends desktop alerts about COVID-19 statistics.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with improvements or bug fixes.

## License

This project is licensed under the MIT License.
