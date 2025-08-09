Imagine

Endpoints related to audiovisual generation.
GET
/images/costs
Get current costs.
Parameters

No parameters
Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "costs": {}
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
GET
/images/mine
Get all images generated under your account.
Parameters
Name	Description
first
integer
(query)
	

The number of the results to get per page.

Default value : 40
page
integer
(query)
	

The page number of the results to get.

Default value : 1
extension_id
integer | (integer | null)
(query)
	
chat_id
integer | (integer | null)
(query)
	
primary_character_id
integer | (integer | null)
(query)
	
parent_image
string | (string | null)
(query)
	
generation_uuid
string | (string | null)
(query)
	
count
boolean | (boolean | null)
(query)
	

Whether to return the total count or not.

Default value : true
include_tts
boolean | (boolean | null)
(query)
	

Whether to include_tts.

Default value : false
generated_only
boolean | (boolean | null)
(query)
	

Whether to return only generated images or not.

Default value : false
Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "count": 0,
  "nodes": [],
  "page": 1
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/images/inpaint
Inpaint an image.
POST
/images/removebg_mask
Remove the background from an image.
Parameters

No parameters
Request body

{
  "seed": 0,
  "extension_source": "string",
  "chat_id": "string",
  "uuid": "string",
  "mode": "string",
  "sub_mode": "string",
  "parent_image": "string",
  "item_id": "string",
  "image": "",
  "alpha_matting": false,
  "post_process_mask": false,
  "alpha_matting_foreground_threshold": 0,
  "alpha_matting_background_threshold": 0,
  "alpha_matting_erode_size": 0
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "generation_uuid": "b9ae-6f64957f986a",
  "cost": 0,
  "queue_length": 0
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/music
Create a new music piece from a prompt.
POST
/tts
Create an audio of the submitted transcript.
Parameters

No parameters
Request body

{
  "seed": 0,
  "extension_source": "string",
  "chat_id": "string",
  "uuid": "string",
  "mode": "string",
  "sub_mode": "string",
  "parent_image": "string",
  "item_id": "string",
  "transcript": "A wizard's job is to vex chumps quickly in fog.",
  "voice_id": "cb65ff32-576b-4c2b-b9ae-6f64957f986a",
  "character_id": null,
  "model": null,
  "remove_silence": true,
  "stream": false
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "generation_uuid": "b9ae-6f64957f986a",
  "cost": 0,
  "queue_length": 0
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
GET
/voices
Get my voices.
Parameters

No parameters
Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "voices": []
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
DELETE
/voices/{voice_id}
Delete voice
Parameters
Name	Description
voice_id *
string
(path)
	
Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "message": "success",
  "success": true
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/voice_clone
Create or update a voice clone.
Parameters

No parameters
Request body
sample
string | (string | null)($binary)
	

The sample audio file. Recognized formats: 'mp3', 'flv', 'ogg', 'wav', 'raw', 'm4a', 'mp4', 'wave'.
transcript
string | (string | null)
	

The text to read out for the example output(s).
model
string | (string | null)
	

Which model to use. all, or None for the default.
reference_text
string | (string | null)
	

Optional. The text that is being said in the sample audio. If not given, stt will be done on the example audio to get this.
character_id_str
string | (string | null)
	

If given, the voice of this character will be set to the voice.
name
string | (string | null)
	

The name of the voice.
existing_id
string | (string | null)
	

The id of the existing voice.
Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "uuid": "string",
  "version": 0,
  "user_id": 0,
  "name": "string",
  "is_done": true,
  "is_failed": true,
  "transcript": "string",
  "sample": "string",
  "reference_text": "string",
  "model": "string",
  "example": "string",
  "e2_example": "string",
  "f5_example": "string",
  "z_example": "string",
  "created_at": "string",
  "updated_at": "string"
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/images/text2img
Create an image from a prompt.
Parameters

No parameters
Request body

{
  "seed": 0,
  "extension_source": "string",
  "chat_id": "string",
  "uuid": "string",
  "mode": "string",
  "sub_mode": "string",
  "parent_image": "string",
  "item_id": "string",
  "prompt": "",
  "negative_prompt": "string",
  "width": 1024,
  "height": 1024,
  "num_inference_steps": 50,
  "guidance_scale": 3.5,
  "aspect_ratio": null,
  "remove_background": false
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "generation_uuid": "b9ae-6f64957f986a",
  "cost": 0,
  "queue_length": 0
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/images/img2img
Create a new image from a base one and a prompt.
Parameters

No parameters
Request body

{
  "seed": 0,
  "extension_source": "string",
  "chat_id": "string",
  "uuid": "string",
  "mode": "string",
  "sub_mode": "string",
  "parent_image": "string",
  "item_id": "string",
  "prompt": "",
  "negative_prompt": "string",
  "width": 1024,
  "height": 1024,
  "num_inference_steps": 50,
  "guidance_scale": 3.5,
  "aspect_ratio": null,
  "init_image": "https://example.com/some_image_url.png",
  "type": "canny",
  "strength": 0.7,
  "remove_background": false
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "generation_uuid": "b9ae-6f64957f986a",
  "cost": 0,
  "queue_length": 0
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/images/animate
Create a new animation from a base image.
Parameters

No parameters
Request body

{
  "seed": 0,
  "extension_source": "string",
  "chat_id": "string",
  "uuid": "string",
  "mode": "string",
  "sub_mode": "string",
  "parent_image": "string",
  "item_id": "string",
  "prompt": "",
  "negative_prompt": "string",
  "width": 1024,
  "height": 1024,
  "num_inference_steps": 50,
  "guidance_scale": 3.5,
  "aspect_ratio": null,
  "init_image": "https://example.com/some_image_url.png",
  "end_image": "string",
  "num_frames": 12,
  "loop": false,
  "fps_id": 8
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "generation_uuid": "b9ae-6f64957f986a",
  "cost": 0,
  "queue_length": 0
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/video
Create a new video from a prompt.
Parameters

No parameters
Request body

{
  "seed": 0,
  "extension_source": "string",
  "chat_id": "string",
  "uuid": "string",
  "mode": "string",
  "sub_mode": "string",
  "parent_image": "string",
  "item_id": "string",
  "prompt": "",
  "negative_prompt": "string",
  "width": 1024,
  "height": 1024,
  "num_inference_steps": 50,
  "guidance_scale": 3.5,
  "aspect_ratio": null,
  "init_image": "https://example.com/some_image_url.png",
  "end_image": "string",
  "num_frames": 12,
  "loop": false,
  "fps_id": 8
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "generation_uuid": "b9ae-6f64957f986a",
  "cost": 0,
  "queue_length": 0
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/foley
Create a new sound effect from a prompt.
Parameters

No parameters
Request body

{
  "seed": 0,
  "extension_source": "string",
  "chat_id": "string",
  "uuid": "string",
  "mode": "string",
  "sub_mode": "string",
  "parent_image": "string",
  "item_id": "string",
  "duration": 4,
  "prompt": "two starships are fighting in space with laser cannons",
  "negative_prompt": "distorted",
  "num_inference_steps": 30
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "generation_uuid": "b9ae-6f64957f986a",
  "cost": 0,
  "queue_length": 0
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/images/upscale
Upscale an image.
Parameters

No parameters
Request body

{
  "seed": 0,
  "extension_source": "string",
  "chat_id": "string",
  "uuid": "string",
  "mode": "string",
  "sub_mode": "string",
  "parent_image": "string",
  "item_id": "string",
  "prompt": "",
  "image": "",
  "negative_prompt": "string",
  "preserve_transparency": true,
  "num_inference_steps": 30
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "generation_uuid": "b9ae-6f64957f986a",
  "cost": 0,
  "queue_length": 0
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/check
Check on a running task.
Parameters

No parameters
Request body

{
  "generation_uuid": "b9ae-6f64957f986a",
  "cost": 0,
  "queue_length": 0,
  "request_type": "string"
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "generation_uuid": "b9ae-6f64957f986a",
  "cost": 0,
  "queue_length": 0
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/stt
STT endpoint.
Parameters

No parameters
Request body
sample *
string($binary)
	

The sample audio file. Recognized formats: 'mp3', 'flv', 'ogg', 'wav', 'raw', 'm4a', 'mp4', 'wave'.
Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "reference_text": ""
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
POST
/prompt
API endpoint for generic completions.
Parameters

No parameters
Request body

{
  "messages": [],
  "model": "mobile",
  "frequency_penalty": 1.15,
  "logit_bias": {},
  "logprobs": false,
  "top_logprobs": 0,
  "max_tokens": 300,
  "max_completion_tokens": 0,
  "n": 1,
  "presence_penalty": 1.15,
  "response_format": {
    "type": "text",
    "json_schema": {
      "name": "string",
      "description": "string",
      "schema": {},
      "strict": true,
      "additionalProp1": {}
    },
    "additionalProp1": {}
  },
  "seed": -9223372036854776000,
  "stop": [],
  "stream": false,
  "stream_options": {
    "include_usage": true,
    "continuous_usage_stats": false,
    "additionalProp1": {}
  },
  "temperature": 0.8,
  "top_p": 1,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "string",
        "description": "string",
        "parameters": {},
        "additionalProp1": {}
      },
      "additionalProp1": {}
    }
  ],
  "tool_choice": "none",
  "parallel_tool_calls": false,
  "user": "string",
  "best_of": 0,
  "use_beam_search": false,
  "top_k": 50,
  "min_p": 0,
  "repetition_penalty": 0,
  "length_penalty": 1,
  "stop_token_ids": [],
  "include_stop_str_in_output": false,
  "ignore_eos": false,
  "min_tokens": 50,
  "skip_special_tokens": true,
  "spaces_between_special_tokens": true,
  "truncate_prompt_tokens": 1,
  "prompt_logprobs": 0,
  "allowed_token_ids": [
    0
  ],
  "bad_words": [
    "string"
  ],
  "echo": false,
  "add_generation_prompt": true,
  "continue_final_message": false,
  "add_special_tokens": false,
  "documents": [
    {
      "additionalProp1": "string",
      "additionalProp2": "string",
      "additionalProp3": "string"
    }
  ],
  "chat_template": "string",
  "chat_template_kwargs": {},
  "mm_processor_kwargs": {},
  "guided_json": "string",
  "guided_regex": "string",
  "guided_choice": [
    "string"
  ],
  "guided_grammar": "string",
  "structural_tag": "string",
  "guided_decoding_backend": "string",
  "guided_whitespace_pattern": "string",
  "priority": 0,
  "request_id": "string",
  "logits_processors": [
    "string",
    {
      "qualname": "string",
      "args": [
        "string"
      ],
      "kwargs": {}
    }
  ],
  "return_tokens_as_token_ids": true,
  "cache_salt": "string",
  "kv_transfer_params": {},
  "vllm_xargs": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "identity": "string",
  "prompt": "string",
  "query": "",
  "typical": 0,
  "token_repetition_penalty": 1.05,
  "guided_decoding": {
    "json": "string",
    "regex": "string",
    "choice": [
      "string"
    ],
    "grammar": "string",
    "json_object": true,
    "backend": "string",
    "backend_was_auto": false,
    "disable_fallback": false,
    "disable_any_whitespace": false,
    "disable_additional_properties": false,
    "whitespace_pattern": "string",
    "structural_tag": "string"
  },
  "sent_at": 0,
  "publish_to": "string",
  "token_repetition_range": -1,
  "token_repetition_decay": 0,
  "top_a": 0,
  "tfs": 0,
  "next": [
    "string"
  ],
  "n_tokens": 0,
  "template": "Hi how are you?",
  "parameters": {},
  "additionalProp1": {}
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "id": "string",
  "object": "chat.completion",
  "created": 0,
  "model": "string",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "string",
        "content": "string",
        "refusal": "string",
        "annotations": {
          "type": "url_citation",
          "url_citation": {
            "end_index": 0,
            "start_index": 0,
            "title": "string",
            "url": "string",
            "additionalProp1": {}
          },
          "additionalProp1": {}
        },
        "audio": {
          "id": "string",
          "data": "string",
          "expires_at": 0,
          "transcript": "string",
          "additionalProp1": {}
        },
        "function_call": {
          "name": "string",
          "arguments": "string",
          "additionalProp1": {}
        },
        "tool_calls": [
          {
            "id": "string",
            "type": "function",
            "function": {
              "name": "string",
              "arguments": "string",
              "additionalProp1": {}
            },
            "additionalProp1": {}
          }
        ],
        "reasoning_content": "string",
        "additionalProp1": {}
      },
      "logprobs": {
        "content": [
          {
            "token": "string",
            "logprob": -9999,
            "bytes": [
              0
            ],
            "top_logprobs": [
              {
                "token": "string",
                "logprob": -9999,
                "bytes": [
                  0
                ],
                "additionalProp1": {}
              }
            ],
            "additionalProp1": {}
          }
        ],
        "additionalProp1": {}
      },
      "finish_reason": "stop",
      "stop_reason": 0,
      "additionalProp1": {}
    }
  ],
  "service_tier": "auto",
  "system_fingerprint": "string",
  "usage": {
    "prompt_tokens": 0,
    "total_tokens": 0,
    "completion_tokens": 0,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "additionalProp1": {}
    },
    "additionalProp1": {}
  },
  "prompt_logprobs": [
    {
      "additionalProp1": {
        "logprob": 0,
        "rank": 0,
        "decoded_token": "string"
      },
      "additionalProp2": {
        "logprob": 0,
        "rank": 0,
        "decoded_token": "string"
      },
      "additionalProp3": {
        "logprob": 0,
        "rank": 0,
        "decoded_token": "string"
      }
    },
    null
  ],
  "kv_transfer_params": {},
  "additionalProp1": {}
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
}

	No links
PATCH
/imagine/project/{uuid}
Update an existing imagine project or image.
Parameters
Name	Description
uuid *
string
(path)
	
Request body

{
  "description": "string",
  "comments_enabled": true,
  "duration": 0,
  "width": 0,
  "height": 0,
  "dpi": 0,
  "z_index": 0,
  "opacity": 0,
  "visible": true,
  "locked": true,
  "start_time": 0,
  "end_time": 0,
  "in_point": 0,
  "out_point": 0,
  "name": "string",
  "parent_image": "string",
  "is_published": true,
  "is_nsfw": true,
  "is_nsfl": true,
  "imagination_type": "string",
  "image": "string",
  "preview": "string",
  "effects": "string"
}

Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "message": "success",
  "success": true
}

	No links
400	

Bad Request
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
401	

Unauthorized
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
403	

Forbidden
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
404	

Not Found
Media type

{
  "error": "",
  "errorCode": 400,
  "code": 0
}

	No links
422	

Validation Error
Media type

{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

	No links
500	

Internal Server Error
Media type

{
  "error": "UNKNOWN",
  "message": "UNKNOWN",
  "type": "UNKNOWN",
  "code": "",
  "errorCode": 500,
  "param": "string"
