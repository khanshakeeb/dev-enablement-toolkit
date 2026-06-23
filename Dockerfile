# Stage 1 — Build
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2 — Runtime
FROM python:3.9-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY cli.py .
COPY modules/ ./modules/

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

ENTRYPOINT ["python", "cli.py"]