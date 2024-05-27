errorlog() {
    echo -e "${RESET}[${RED}${BLINK}ERROR${STOPBLINK}${RESET}] $1" && sleep 0.2
}
warnlog() {
    echo -e "${RESET}[${YELLOW}WARN${RESET}] $1" && sleep 0.2
}
successlog() {
    echo -e "${RESET}[${GREEN}SUCCESS${RESET}] $1" && sleep 0.2
}
infolog() {
    echo -e "${RESET}[${CYAN}INFO${RESET}] $1" && sleep 0.2
}
sublog() {
    echo -e "\t${RESET}${MAGENTA}ㄷ ${WHITE}$1" && sleep 0.2
}
setline() {
    # Get the size of the terminal
    local columns=$(tput cols)
    local total=""
    for ((i=1; i<=$columns; i++)); do
        total+="-"
    done
    echo -e "$1$total"
}