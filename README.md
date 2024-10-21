# Academic Calendar

An academic calendar application that allows users to manage and organize events throughout the academic year. This application provides features such as adding, updating, and deleting events, along with a visual calendar interface.

## Features

- Add events with specific dates
- Update existing events
- Delete events
- Visual calendar for date selection
- User-friendly interface

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Tkinter (usually comes with Python installations)
- Additional packages specified in `requirements.txt`

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd Academic Calendar

----------
TR Des.
-----------
### Açıklamalar:
- **Features**: Uygulamanızın özelliklerini listeledik.
- **Prerequisites**: Gerekli yazılımları ve kütüphaneleri belirttik.
- **Installation**: Projeyi yerel makinenize kurma adımlarını açıkladık.
- **Usage**: Uygulamanın nasıl kullanılacağını detaylandırdık.
- **Database**: Kullanılan veritabanı hakkında bilgi verdik.
- **License** ve **Contributing**: Projenizin lisansı ve katkıda bulunmak isteyenler için bilgiler ekledik.
- **Acknowledgments**: Kullanılan kütüphaneleri belirttik.

Bu örneği kendi projenize göre özelleştirebilirsiniz! Eğer başka bir konuda yardıma ihtiyacınız olursa, lütfen belirtin.


1- python -m venv .venv
2-.venv\Scripts\activate
3-source .venv/bin/activate
4-pip install -r requirements.txt

 Run python main.py


Usage
Upon launching the application, you'll see the main interface with a calendar and event input fields.
Select a date from the calendar.
Enter the event details in the input field.
Click "Add Event" to save the event.
To update or delete an event, select it from the event list and use the corresponding buttons.
Database
The application uses a SQLite database (academic_calendar.db) to store event information. The database is automatically created upon the first run of the application.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

Acknowledgments
Tkinter for GUI development
tkcalendar for calendar widget
Pillow for image handling