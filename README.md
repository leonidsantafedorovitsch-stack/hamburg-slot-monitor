# Hamburg Slot Monitor

Real-time monitoring of container terminal slot availability at Hamburg ports.  
Monitors all 14 terminals in the TR02-TruckGATE network via the public [slot.truckgate.de](https://slot.truckgate.de) API.

## Features

- **14 terminals** — Eurogate CTH/EKOM/CTB/CTW, HHLA CTA/CTB/CTT, C. Steinweg, CPA, VETI, HCS, CMR, CCIS Germany + Bremerhaven & Wilhelmshaven
- **Auto-refresh** — polls every 45–75 seconds with randomized interval
- **Terminal monitoring** — select a specific terminal, time range, and operation type
- **Operation filters:**
  - Voll einliefern (full container drop-off)
  - Voll ausliefern (full container pickup)
  - Leer einliefern (empty container drop-off)
  - Leer ausliefern (empty container pickup)
- **Sound alerts** — three loud beeps when a slot becomes available
- **Push notifications** — browser notifications for new free slots
- **Gate-level detail** — per-gate breakdown for HHLA terminals (Anlieferung/Auslieferung)
- **Color coding** — green (free), yellow (warning), red (full), gray (unrestricted)
- **Filters** — by city (Hamburg/Bremerhaven/Wilhelmshaven), availability status
- **Log panel** — history of all updates and alerts
- **Responsive** — works on mobile and desktop

## Usage

Open `index.html` directly in a browser — no server required.

Or serve locally:
```bash
python server.py
# Open http://localhost:8080
```

## How it works

The app fetches data from two public API endpoints (no authentication required):

| Endpoint | Description |
|---|---|
| `GET /slot-web/api/terminals` | List of all terminals |
| `GET /slot-web/api/slotauslastungen` | Slot occupancy data |

### Slot availability codes

| Code | Meaning |
|---|---|
| 0 | Available (capacity management active) |
| 1 | Warning — nearly full |
| 2 | Full — no bookings possible |
| 3 | Unrestricted — outside managed hours |

## Tech stack

- Single-file HTML/CSS/JS (no dependencies)
- Web Audio API for sound alerts
- Notification API for push
- Fetch API for data

## License

MIT
