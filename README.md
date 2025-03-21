# CarPlay and Android Auto Compatibility API

A simple Flask API that provides information about vehicles compatible with Apple CarPlay and Android Auto.

## Overview

This API allows developers to retrieve up-to-date information about:
- Vehicles supporting Apple CarPlay
- Vehicles supporting Android Auto
- Combined data for both platforms

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home page |
| `/carplay-vehicles` | Returns all CarPlay compatible vehicles |
| `/android-auto-vehicles` | Returns all Android Auto compatible vehicles |
| `/all-vehicles` | Returns combined data for both platforms |

## Getting Started

### Prerequisites
- Python 3.6+
- Flask

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/carplay-androidauto-api.git
cd carplay-androidauto-api
```

2. Install dependencies
```bash
pip install flask
```

3. Run the application
```bash
python app.py
```

The API will be available at `http://localhost:5000/`

## Usage Examples

### Get CarPlay Compatible Vehicles
```bash
curl http://localhost:5000/carplay-vehicles
```

### Get Android Auto Compatible Vehicles
```bash
curl http://localhost:5000/android-auto-vehicles
```

### Get All Compatible Vehicles
```bash
curl http://localhost:5000/all-vehicles
```

## Project Structure

```
carplay-androidauto-api/
├── app.py                  # Main Flask application
├── lib/
│   ├── carplay.py          # CarPlay data functions
│   └── androidauto.py      # Android Auto data functions
└── templates/
    └── index.html          # Homepage template
```

## Development

Run the application in debug mode:
```bash
python app.py
```

## License

[MIT](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
