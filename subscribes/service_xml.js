const redis = require("redis");
const jsonxml = require("jsontoxml");
const fs = require("fs");

const subscriber = redis.createClient();

subscriber.on("message", function (channel, message) {
  let xml = jsonxml(message);
  fs.writeFile("./files/file_js.xml", xml, function (err) {
    if (err) {
      return console.log(err);
    }
    console.log("File node XML");
  });
});

subscriber.subscribe("topic_create_file");
