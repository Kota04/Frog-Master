#!/bin/bash

install_tshark() {
    if command -v tshark &> /dev/null; then
        echo "TShark is already installed."
    else
        if [ -f /etc/os-release ]; then
            . /etc/os-release
            case "$ID" in
                ubuntu|debian)
                    echo "Detected Debian-based distribution. Installing TShark..."
                    sudo apt-get update
                    sudo apt-get install -y tshark
                    ;;
                fedora)
                    echo "Detected Fedora. Installing TShark..."
                    sudo dnf install -y wireshark-cli
                    ;;
                arch)
                    echo "Detected Arch Linux. Installing TShark..."
                    sudo pacman -Syu --noconfirm wireshark-qt
                    ;;
                *)
                    echo "Unsupported Linux distribution: $ID"
                    echo "Please install TShark manually."
                    exit 1
                    ;;
            esac
        else
            echo "Cannot detect Linux distribution. Please install TShark manually."
            exit 1
        fi
    fi
}

# Install pip and Python development packages if not already installed
if ! command -v pip3 &> /dev/null; then
    echo "Installing pip and Python development packages..."
    sudo apt-get install -y python3-pip python3-dev
else
    echo "pip and Python development packages are already installed."
fi

# Install customtkinter and Pillow using pip if not already installed
pip_install() {
    PACKAGE=$1
    if ! pip3 show "$PACKAGE" &> /dev/null; then
        echo "Installing $PACKAGE..."
        pip3 install "$PACKAGE"
    else
        echo "$PACKAGE is already installed."
    fi
}

pip_install customtkinter
pip_install pillow

# Install TShark
install_tshark

# Install iproute2 if not already installed
if ! command -v ip &> /dev/null; then
    echo "Installing iproute2 package..."
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        case "$ID" in
            ubuntu|debian)
                sudo apt-get update
                sudo apt-get install -y iproute2
                ;;
            fedora)
                sudo dnf install -y iproute
                ;;
            arch)
                sudo pacman -Syu --noconfirm iproute2
                ;;
            *)
                echo "Unsupported Linux distribution: $ID"
                echo "Please install iproute2 manually."
                exit 1
                ;;
        esac
    else
        echo "Cannot detect Linux distribution. Please install iproute2 manually."
        exit 1
    fi
else
    echo "iproute2 is already installed."
fi

# Verify installations
echo "Verifying installations..."

echo "Python packages:"
pip3 list | grep -E 'customtkinter|Pillow'

echo "TShark version:"
tshark --version

echo "Installation complete."
