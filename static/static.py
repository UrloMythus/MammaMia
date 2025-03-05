# static.py

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mamma Mia</title>
    <link rel="icon" href="https://creazilla-store.fra1.digitaloceanspaces.com/emojis/49647/pizza-emoji-clipart-md.png" type="image/x-icon">
    <title>Fast Search Example</title>
    <style>
        * {
            box-sizing: border-box;
        }
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            font-size: 2.2vh;
            font-family: 'Open Sans', Arial, sans-serif;
            color: white;
            background: url('https://i.postimg.cc/ry3p76HY/italian-seamless-free-vector-pattern3.png') center center repeat;
            background-size: cover;
            display: flex;
            align-items: flex-start;
            justify-content: center;
            overflow-y: auto;
        }
        #addon {
            background: rgba(0, 0, 0, 0.8);
            padding: 0.5vh;
            border-radius: 10px;
            width: 65vh;
            max-width: 100%;
            text-align: center;
            margin-top: 10vh;
        }
        .logo {
            width: 12vh;
            margin: 0 auto;
            margin-bottom: 3vh;
            margin-top: -3vh;
        }
        .logo img {
            width: 100%;
            height: auto;
        }
        h1, h2, h3 {
            margin: 0;
            text-shadow: 0 0 1vh rgba(0, 0, 0, 0.15);
        }
        h1 {
            font-size: 4.5vh;
            font-weight: 700;
        }
        h2 {
            font-size: 2vh;
            font-weight: normal;
            font-style: italic;
            opacity: 0.8;
            margin-bottom: 20px;
        }
        h3 {
            font-size: 2.2vh;
            margin-bottom: 10px;
        }
        .provider-group {
            display: flex;
            align-items: center; /* Vertically align items */
            justify-content: space-between; /* Spread items across the available space */
            margin-bottom: 2vh;
            background: rgba(255, 255, 255, 0.1);
            padding: 1.5vh;
            border-radius: 5px;
            overflow: hidden;
            width: 100%;
        }
        .provider-group label {
            display: flex;
            align-items: center; /* Align items within label vertically centered */
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            flex-grow: 1; /* Let the label take as much space as possible */
            font-size: 2.2vh;
        }
        .fast-search {
            display: flex;
            align-items: center; /* Align the Fast Search checkbox vertically centered */
            margin-left: 10px; /* Space between provider and Fast Search */
        }
        .fast-search input[type="checkbox"] {
            margin-right: 0.5vh; /* Space between the checkbox and label */
            width: 3vh;
            height: 3vh;
        }
        .provider-group input[type="checkbox"] {
            margin-right: 1.5vh;
            width: 4vh;
            height: 4vh;
        }
        .parent-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
        }
        .contact {
            position: absolute;
            left: 0;
            bottom: 4vh;
            width: 100%;
            text-align: center;
        }
        .contact a {
            font-size: 1.4vh;
            font-style: italic;
        }
        button {
            border: 0;
            outline: 0;
            color: white;
            background: #8A5AAB;
            padding: 1.2vh 3.5vh;
            text-align: center;
            font-family: 'Open Sans', Arial, sans-serif;
            font-size: 2.2vh;
            font-weight: 600;
            cursor: pointer;
            display: block;
            box-shadow: 0 0.5vh 1vh rgba(0, 0, 0, 0.2);
            transition: box-shadow 0.1s ease-in-out;
            width: 80%;
            max-width: 35vh;
            margin: 1vh auto;
        }
        button:hover {
            box-shadow: none;
        }
        button:active {
            box-shadow: 0 0 0 0.5vh white inset;
        }
        #manifestBox {
            margin-top: 2vh;
            padding: 2vh;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 5px;
            display: none;
            text-align: left;
            white-space: pre-wrap;
        }
        #generateManifestButton {
            background: #4CAF50;
        }
        #installButton {
            background: #FF5722;
        }
        #installButton a {
            color: white;
            text-decoration: none;
        }
        #additionalText {
            margin-top: 2vh;
            font-size: 1.8vh;
            text-align: left;
        }
        /* Responsive adjustments for smaller screens */
        @media (max-width: 600px) {
            .provider-group label {
                font-size: 2vh;
                white-space: nowrap;
            }
        }
    </style>
</head>
<body>
    <div id="addon">
        <div class="logo">
            <img src="https://creazilla-store.fra1.digitaloceanspaces.com/emojis/49647/pizza-emoji-clipart-md.png" alt="Logo">
        </div>
        <h1 class="name">Mamma Mia</h1>
        <h2 class="version">v1.5.0</h2>
        <div id="additionalText">
            <h2>This addon provides Movie, Series, Anime, and Live TV HTTPS Streams.<br> https://github.com/UrloMythus/MammaMia/</h2>
        </div>
        <p class="description">Configure your providers: Note that if you enable Fast Search results will be less accurate but faster</p>
        <h3 class="gives">Select Providers:</h3>
        <form class="pure-form" id="provider-form">
            <div class="provider-group">
                <label for="lordchannel" class="provider-label">
                    <input type="checkbox" id="lordchannel"> LordChannel
                </label>
            </div>
            <div class="provider-group">
                <label for="streamingwatch" class="provider-label">
                    <input type="checkbox" id="streamingwatch"> StreamingWatch
                </label>
            </div>
            <div class="provider-group">
                <label for="animeworld" class="provider-label">
                    <input type="checkbox" id="animeworld"> Animeworld
                </label>
            </div>
            <p>To use the following provider you need to have a local instance/ set the proxy enviroment variable... Leave it as it is if you do not know what this is about
            </p>
            <div class="provider-group">
                <label for="guardaserie" class="provider-label">
                    <input type="checkbox" id="guardaserie"> Guardaserie
                </label>
            </div>
            <div class="provider-group">
                <label for="guardahd" class="provider-label">
                    <input type="checkbox" id="guardahd"> GuardaHD
                </label>
            </div>
            <div class="provider-group">
                <label for="guardahd" class="provider-label">
                    <input type="checkbox" id="onlineserietv"> OnlineSerieTV
                </label>
            </div>
            <div class="provider-group">
                <label for="tantifilm" class="provider-label">
                    <input type="checkbox" id="tantifilm"> Tantifilm
                </label>
                <span class="fast-search">
                    <label for="fast_search_tf">
                        <input type="checkbox" id="fast_search_tf"> Fast Search
                    </label>
                </span>
             </div>
          <div>
            <p>To use the following providers you need to use a local instance or else you need to set up Mediaflow-proxy... Search it on GitHub
            </p>
            </div>
            <div class="provider-group">
                <label for="filmpertutti" class="provider-label">
                    <input type="checkbox" id="filmpertutti"> 
                    Filmpertutti
                </label>
            </div>
          
            <div class="provider-group">
                <label for="cb01" class="provider-label">
                    <input type="checkbox" id="cb01"> CB01
                </label>
            </div>
             <div class="provider-group">
                <label for="ddlstream" class="provider-label">
                    <input type="checkbox" id="ddlstream"> DDLStream Italy
                </label>
            </div>
            <p>To use the following provider you need to use a local instance or else you need to set up Mediaflow-proxy with an IP not blocked by the site</p>
            <div class="provider-group">
                <label for="streamingcommunity" class="provider-label">
                    <input type="checkbox" id="streamingcommunity"> StreamingCommunity
                </label>
                <span class="fast-search">
                    <label for="fast_search_sc">
                        <input type="checkbox" id="fast_search_sc"> Fast Search
                    </label>
                </span>
            </div>
            <div class="provider-group">
                <label for="livetv" class="provider-label">
                    <input type="checkbox" id="livetv"> LiveTV
                </label>
            </div>
            <div class="provider-group">
                <label for="mediaflowproxy" class="provider-label">
                    <input type="checkbox" id="mediaflowproxy"> MediaFlow Proxy
                </label>
                <button type="button" id="mediaFlowProxyButton">Insert Proxy Info</button>
            </div>
            <div id="mediaFlowProxyInputContainer" style="display: none;">
                <input type="text" id="mediaFlowProxyInput" placeholder="Proxy URL">
            </div>
            <div id="mediaFlowProxyPasswordContainer" style="display: none;">
                <input type="password" id="mediaFlowProxyPassword" placeholder="Insert Password">
            </div>
        </form>
        <button id="generateManifestButton">Generate Manifest</button>
        <div id="manifestBox"></div>
        <button id="installButton">Install in Stremio</button>
    </div>
    <script>
        // Toggle visibility of proxy input fields
    document.getElementById('mediaFlowProxyButton').addEventListener('click', function() {
        const inputContainer = document.getElementById('mediaFlowProxyInputContainer');
        const passwordInputContainer = document.getElementById('mediaFlowProxyPasswordContainer');
        inputContainer.style.display = inputContainer.style.display === 'none' ? 'block' : 'none';
        passwordInputContainer.style.display = passwordInputContainer.style.display === 'none' ? 'block' : 'none';
    });

    // Function to generate the manifest URL
    function generateManifest() {
        let manifest = "|";
        const providers = {
            "streamingcommunity": "SC",
            "fast_search_sc": "SC_FS",
            "lordchannel": "LC",
            "streamingwatch": "SW",
            "tantifilm": "TF",
            "fast_search_tf": "TF_FS",
            "filmpertutti": "FT",
            "animeworld": "AW",
            "livetv": "LIVETV",
            "cb01": "CB",
            "ddlstream": "DDL",
            "guardaserie": "GS",
            "guardahd": "GHD",
            "onlineserietv": "OST",
            "mediaflowproxy": "MFP"
        };

        // Loop through providers and add selected ones to the manifest
        for (const id in providers) {
            if (document.getElementById(id).checked) {
                if (id === "mediaflowproxy") {
                    // Add proxy details if MFP is selected
                    const proxyUrl = document.getElementById("mediaFlowProxyInput").value.trim();
                    const proxyPassword = document.getElementById("mediaFlowProxyPassword").value.trim();
                    if (proxyUrl && proxyPassword) {
                        manifest += `MFP[${proxyUrl},${proxyPassword}]|`;
                    } else {
                        manifest += providers[id] + "|"; // Fallback to just "MFP" if no details provided
                    }
                } else {
                    manifest += providers[id] + "|";
                }
            }
        }

        const instanceUrl = "{instance_url}"; // Replace with your instance URL
        const manifestUrl = instanceUrl + "/" + manifest + "/" + "manifest.json";
        return manifestUrl;
    }

    // Generate manifest URL and display it
    document.getElementById('generateManifestButton').addEventListener('click', function() {
        const manifestUrl = generateManifest();
        const manifestBox = document.getElementById("manifestBox");
        manifestBox.style.display = "block";
        manifestBox.innerText = manifestUrl;
    });

    // Install the manifest in Stremio
    document.getElementById('installButton').addEventListener('click', function() {
        let manifestUrl = generateManifest();
        manifestUrl = manifestUrl.replace("http://", "");
        manifestUrl = manifestUrl.replace("https://", "");
        const stremioUrl = "stremio://" + manifestUrl;
        window.location.href = stremioUrl;
    });
    </script>
</body>
</html>
"""