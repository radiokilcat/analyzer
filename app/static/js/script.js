function stateToColor(state) {
    switch (state) {
        case "offline":
            return "red";
        case "online":
        case "playback":
            return "green";
        default:
            return "gray";
    }
}