# Acme Inventory API

Internal inventory management API for Acme Corp's warehouse operations.

## Development

This project uses GitHub Codespaces for standardized development environments.

### Quick Start

1. Click "Code" → "Codespaces" → "Create codespace on main"
2. Wait for the environment to build (~2 minutes)
3. Run the API: `flask run`
4. Access at http://localhost:5000

### API Endpoints

- `GET /api/inventory` - List all inventory items
- `GET /api/inventory/<id>` - Get specific item
- `POST /api/inventory` - Create new item
- `GET /api/users/<id>` - Get user details
- `GET /api/export/<filename>` - Export inventory report

### Running Tests

```bash
pytest tests/ -v
```

## Security

This repository has GitHub Advanced Security enabled:
- Secret scanning
- Code scanning (CodeQL)
- Dependabot alerts
