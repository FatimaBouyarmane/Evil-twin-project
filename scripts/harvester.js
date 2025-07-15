function onRequest(req, res) {
    if (req.method == "POST") {
        var body = req.body;
        console.log("[HARVESTER] Data: " + JSON.stringify(body));
    }
}
