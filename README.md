# Hamburg Slot Monitor

Real-time monitoring of container terminal slot availability at Hamburg ports.

![Screenshot](screenshot.png)

## About

This tool monitors all 14 container terminals in the Hamburg TR02-TruckGATE network, helping truck dispatchers find available time slots for container drop-off and pickup operations. Data is sourced from the public [slot.truckgate.de](https://slot.truckgate.de) API — no registration required.

## Monitored Terminals

| Terminal | Code | Location |
|---|---|---|
| Eurogate CTH | EGH | Hamburg |
| Eurogate EKOM | EKOM | Hamburg |
| Eurogate CTB | EGB | Bremerhaven |
| Eurogate CTW | EGW | Wilhelmshaven |
| HHLA CTA | CTA | Hamburg |
| HHLA CTB | BK | Hamburg |
| HHLA CTT | TCT | Hamburg |
| C. Steinweg | SWT | Hamburg |
| CPA Hamburg | CPAH | Hamburg |
| VETI Altenwerder | VETA | Hamburg |
| VETI Reiherdamm | VETR | Hamburg |
| HCS | HCS | Hamburg |
| CMR | CMR2 | Hamburg |
| CCIS Germany | GECO | Hamburg |

## Features

- **Auto-refresh** — polls every 45–75 seconds with randomized interval
- **Terminal monitoring** — select a specific terminal, time range, and operation type
- **Operation filters:**
  - Voll einliefern — full container drop-off (Anlieferung)
  - Voll ausliefern — full container pickup (Auslieferung)
  - Leer einliefern — empty container drop-off (Anlieferung leer)
  - Leer ausliefern — empty container pickup (Leerlager)
- **Sound alerts** — three loud beeps when a slot becomes available
- **Push notifications** — browser notifications for new free slots
- **Gate-level detail** — per-gate breakdown for HHLA terminals
- **Color coding** — green (free), yellow (warning), red (full), gray (unrestricted)
- **Filters** — by city (Hamburg/Bremerhaven/Wilhelmshaven), availability status
- **Log panel** — history of all updates and alerts
- **Responsive** — works on mobile and desktop

## Quick Start

Open `index.html` directly in a browser — no server required.

Or serve locally:
```bash
python server.py
# Open http://localhost:8080
```

## How It Works

The app fetches data from two public API endpoints (no authentication required):

| Endpoint | Description |
|---|---|
| `GET /slot-web/api/terminals` | List of all terminals |
| `GET /slot-web/api/slotauslastungen` | Slot occupancy data |

### Slot Availability Codes

| Code | Meaning |
|---|---|
| 0 | Available (capacity management active) |
| 1 | Warning — nearly full |
| 2 | Full — no bookings possible |
| 3 | Unrestricted — outside managed hours |

## Tech Stack

- Single-file HTML/CSS/JS — no build tools, no dependencies
- Web Audio API for sound alerts
- Notification API for push notifications
- Fetch API for data retrieval

## License

MIT
