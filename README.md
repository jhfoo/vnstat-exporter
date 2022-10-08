# vnstat-exporter
1. Prometheus exporter for [vnstat](https://www.cyberciti.biz/faq/freebsd-install-vnstat-network-traffic-monitor-software/).
2. Returns 5-min intervals of averaged rx and tx speed.

## Requirements
1. FreeBSD 13.1-RELEASE (tested).
2. vnstat installed, configured, and running.
3. zsh as default shell (tested).
4. Python 3.9 installed.

## Install
```
git clone https://github.com/jhfoo/vnstat-exporter.git
cd vnstat-exporter
./bin/install
```

## Run
```
cd vnstat-exporter
./bin/start
# listens on port 8080 at /api/prometheus
```

## Todo
1. Make it daemon-able without using gunicorn (capture access logs)
2. Make host, port, and path configurable (yaml?)