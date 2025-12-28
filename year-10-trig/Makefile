# Makefile for generating PDF from Year 10 Trig Revision Guide
# Requires: pandoc, texlive-latex-base, texlive-latex-extra, librsvg2-bin

# Variables
SOURCE = Year_10_Trig_Revision_Guide.md
OUTPUT = Year_10_Trig_Revision_Guide.pdf
PANDOC = pandoc
PANDOC_FLAGS = --pdf-engine=xelatex \
               --toc \
               --toc-depth=2 \
               --number-sections \
               --highlight-style=tango \
               --include-in-header=header.tex \
               --variable=geometry:margin=2.5cm \
               --variable=fontsize:11pt \
               --variable=documentclass:article \
               --variable=papersize:a4 \
               --variable=colorlinks:true \
               --variable=linkcolor:blue \
               --variable=urlcolor:blue \
               --variable=toccolor:black \
               -V mainfont="DejaVu Serif" \
               -V monofont="DejaVu Sans Mono" \
               -V mathfont="DejaVu Math TeX Gyre"

# Default target
.PHONY: all
all: pdf

# Generate PDF
.PHONY: pdf
pdf: $(OUTPUT)

$(OUTPUT): $(SOURCE)
	@echo "Generating PDF from $(SOURCE)..."
	$(PANDOC) $(SOURCE) -o $(OUTPUT) $(PANDOC_FLAGS)
	@echo "PDF generated: $(OUTPUT)"

# Quick view the PDF (Linux)
.PHONY: view
view: $(OUTPUT)
	@if command -v xdg-open >/dev/null 2>&1; then \
		xdg-open $(OUTPUT); \
	elif command -v evince >/dev/null 2>&1; then \
		evince $(OUTPUT) & \
	elif command -v okular >/dev/null 2>&1; then \
		okular $(OUTPUT) & \
	else \
		echo "No PDF viewer found. Please open $(OUTPUT) manually."; \
	fi

# Clean generated files
.PHONY: clean
clean:
	@echo "Removing generated files..."
	rm -f $(OUTPUT)
	rm -f *.aux *.log *.out *.toc
	@echo "Clean complete."

# Force rebuild
.PHONY: rebuild
rebuild: clean pdf

# Check dependencies
.PHONY: check-deps
check-deps:
	@echo "Checking dependencies..."
	@command -v pandoc >/dev/null 2>&1 || (echo "ERROR: pandoc not found. Install with: sudo apt install pandoc" && exit 1)
	@command -v xelatex >/dev/null 2>&1 || (echo "ERROR: xelatex not found. Install with: sudo apt install texlive-xetex texlive-latex-extra" && exit 1)
	@command -v rsvg-convert >/dev/null 2>&1 || (echo "WARNING: rsvg-convert not found. SVG support may be limited. Install with: sudo apt install librsvg2-bin" && exit 0)
	@echo "All required dependencies found!"

# ============================================
# Docker targets (no local dependencies needed)
# ============================================

# Build Docker image
.PHONY: docker-build
docker-build:
	@echo "Building Docker image..."
	docker build -t year10-trig-pdf .
	@echo "Docker image built successfully!"

# Generate PDF using Docker
.PHONY: docker-pdf
docker-pdf:
	@echo "Generating PDF using Docker..."
	docker run --rm -v "$(PWD):/workspace" year10-trig-pdf make pdf
	@echo "PDF generated using Docker!"

# Generate PDF using docker-compose (easier)
.PHONY: docker-compose-pdf
docker-compose-pdf:
	@echo "Generating PDF using docker-compose..."
	docker-compose up --build
	@echo "PDF generated using docker-compose!"

# Interactive shell in Docker container
.PHONY: docker-shell
docker-shell:
	@echo "Starting interactive shell in Docker container..."
	docker run --rm -it -v "$(PWD):/workspace" year10-trig-pdf /bin/bash

# Clean Docker images
.PHONY: docker-clean
docker-clean:
	@echo "Removing Docker image..."
	docker rmi year10-trig-pdf 2>/dev/null || true
	@echo "Docker cleanup complete."

# Help target
.PHONY: help
help:
	@echo "Year 10 Trigonometry Revision Guide - PDF Generator"
	@echo ""
	@echo "=== Local Build (requires dependencies) ==="
	@echo "  make pdf              - Generate PDF from markdown (default)"
	@echo "  make view             - Generate and open PDF in viewer"
	@echo "  make clean            - Remove generated PDF and temp files"
	@echo "  make rebuild          - Clean and regenerate PDF"
	@echo "  make check-deps       - Check if required tools are installed"
	@echo ""
	@echo "=== Docker Build (no local dependencies needed) ==="
	@echo "  make docker-build     - Build Docker image with all dependencies"
	@echo "  make docker-pdf       - Generate PDF using Docker"
	@echo "  make docker-compose-pdf - Generate PDF using docker-compose (recommended)"
	@echo "  make docker-shell     - Open interactive shell in Docker container"
	@echo "  make docker-clean     - Remove Docker image"
	@echo ""
	@echo "  make help             - Show this help message"
	@echo ""
	@echo "Quick Start with Docker:"
	@echo "  make docker-compose-pdf"
	@echo ""
	@echo "Local Requirements:"
	@echo "  - pandoc        (sudo apt install pandoc)"
	@echo "  - xelatex       (sudo apt install texlive-xetex texlive-latex-extra)"
	@echo "  - rsvg-convert  (sudo apt install librsvg2-bin) [optional]"
