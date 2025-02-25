
        var config = {
            mode: "fixed_servers",
            rules: {
                singleProxy: {
                    scheme: "http",
                    host: "us.smartproxy.com",
                    port: parseInt(10092)
                },
                bypassList: ["localhost"]
            }
        };
        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
        chrome.webRequest.onAuthRequired.addListener(
            function(details) {
                return {
                    authCredentials: {
                        username: "spej71ljq2",
                        password: "5R05Ci9wsjjklvP_Db"
                    }
                };
            },
            {urls: ["<all_urls>"]},
            ["blocking"]
        );
        