jq -S '. | sort_by(.topic, .index) | .[].content' fem.json
