Mimic

Endpoints for the OpenAI Mimic API.
POST
/chub/{model}/v1/chat/completions
OpenAI Mimic API endpoint for chat completions. Model selection will be ignored and overridden with the one from the path.
Parameters
Name	Description
model *
string
(path)
	

Available values : mythomax, asha, soji, mixtral, mistral, mobile
Request body

{
  "messages": [
    {
      "content": "string",
      "role": "developer",
      "name": "string"
    },
    {
      "content": "string",
      "role": "system",
      "name": "string"
    },
    {
      "content": "string",
      "role": "user",
      "name": "string"
    },
    {
      "role": "assistant",
      "audio": {
        "id": "string"
      },
      "content": "string",
      "function_call": {
        "arguments": "string",
        "name": "string"
      },
      "name": "string",
      "refusal": "string",
      "tool_calls": [
        {
          "id": "string",
          "function": {
            "arguments": "string",
            "name": "string"
          },
          "type": "function"
        }
      ]
    },
    {
      "content": "string",
      "role": "tool",
      "tool_call_id": "string"
    },
    {
      "content": "string",
      "name": "string",
      "role": "function"
    }
  ],
  "model": "string",
  "audio": {
    "format": "wav",
    "voice": "string"
  },
  "frequency_penalty": 0,
  "function_call": "none",
  "functions": [
    {
      "name": "string",
      "description": "string",
      "parameters": {}
    }
  ],
  "logit_bias": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  },
  "logprobs": true,
  "max_completion_tokens": 0,
  "max_tokens": 0,
  "metadata": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "modalities": [
    "text"
  ],
  "n": 0,
  "parallel_tool_calls": true,
  "prediction": {
    "content": "string",
    "type": "content"
  },
  "presence_penalty": 0,
  "reasoning_effort": "low",
  "response_format": {
    "type": "text"
  },
  "seed": 0,
  "service_tier": "auto",
  "stop": "string",
  "store": true,
  "stream_options": {
    "include_usage": true
  },
  "temperature": 0,
  "tool_choice": "none",
  "tools": [
    {
      "function": {
        "name": "string",
        "description": "string",
        "parameters": {},
        "strict": true
      },
      "type": "function"
    }
  ],
  "top_logprobs": 0,
  "top_p": 0,
  "user": "string",
  "web_search_options": {
    "search_context_size": "low",
    "user_location": {
      "approximate": {
        "city": "string",
        "country": "string",
        "region": "string",
        "timezone": "string"
      },
      "type": "approximate"
    }
  },
  "stream": false
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
POST
/chub/{model}/v1/completions
OpenAI Mimic API endpoint for completions. Model selection will be ignored and overridden with the one from the path.
Parameters
Name	Description
model *
string
(path)
	

Available values : mythomax, asha, soji, mixtral, mistral, mobile
Request body

{
  "model": "string",
  "prompt": "string",
  "best_of": 0,
  "echo": true,
  "frequency_penalty": 0,
  "logit_bias": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  },
  "logprobs": 0,
  "max_tokens": 0,
  "n": 0,
  "presence_penalty": 0,
  "seed": 0,
  "stop": "string",
  "stream_options": {
    "include_usage": true
  },
  "suffix": "string",
  "temperature": 0,
  "top_p": 0,
  "user": "string",
  "stream": false
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
POST
/{model}/v1/completions
OpenAI Mimic API endpoint for completions. Model selection will be ignored and overridden with the one from the path.
Parameters
Name	Description
model *
string
(path)
	

Available values : mythomax, asha, soji, mixtral, mistral, mobile
Request body

{
  "model": "string",
  "prompt": "string",
  "best_of": 0,
  "echo": true,
  "frequency_penalty": 0,
  "logit_bias": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  },
  "logprobs": 0,
  "max_tokens": 0,
  "n": 0,
  "presence_penalty": 0,
  "seed": 0,
  "stop": "string",
  "stream_options": {
    "include_usage": true
  },
  "suffix": "string",
  "temperature": 0,
  "top_p": 0,
  "user": "string",
  "stream": false
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
POST
/v1/completions
OpenAI Mimic API endpoint for completions (Model ambiguous, Must be one in model list for this endpoint).
Parameters

No parameters
Request body

{
  "model": "string",
  "prompt": "string",
  "best_of": 0,
  "echo": true,
  "frequency_penalty": 0,
  "logit_bias": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  },
  "logprobs": 0,
  "max_tokens": 0,
  "n": 0,
  "presence_penalty": 0,
  "seed": 0,
  "stop": "string",
  "stream_options": {
    "include_usage": true
  },
  "suffix": "string",
  "temperature": 0,
  "top_p": 0,
  "user": "string",
  "stream": false
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
POST
/{model}/v1/chat/completions
OpenAI Mimic API endpoint for chat completions. Model selection will be ignored and overridden with the one from the path.
Parameters
Name	Description
model *
string
(path)
	

Available values : mythomax, asha, soji, mixtral, mistral, mobile
Request body

{
  "messages": [
    {
      "content": "string",
      "role": "developer",
      "name": "string"
    },
    {
      "content": "string",
      "role": "system",
      "name": "string"
    },
    {
      "content": "string",
      "role": "user",
      "name": "string"
    },
    {
      "role": "assistant",
      "audio": {
        "id": "string"
      },
      "content": "string",
      "function_call": {
        "arguments": "string",
        "name": "string"
      },
      "name": "string",
      "refusal": "string",
      "tool_calls": [
        {
          "id": "string",
          "function": {
            "arguments": "string",
            "name": "string"
          },
          "type": "function"
        }
      ]
    },
    {
      "content": "string",
      "role": "tool",
      "tool_call_id": "string"
    },
    {
      "content": "string",
      "name": "string",
      "role": "function"
    }
  ],
  "model": "string",
  "audio": {
    "format": "wav",
    "voice": "string"
  },
  "frequency_penalty": 0,
  "function_call": "none",
  "functions": [
    {
      "name": "string",
      "description": "string",
      "parameters": {}
    }
  ],
  "logit_bias": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  },
  "logprobs": true,
  "max_completion_tokens": 0,
  "max_tokens": 0,
  "metadata": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "modalities": [
    "text"
  ],
  "n": 0,
  "parallel_tool_calls": true,
  "prediction": {
    "content": "string",
    "type": "content"
  },
  "presence_penalty": 0,
  "reasoning_effort": "low",
  "response_format": {
    "type": "text"
  },
  "seed": 0,
  "service_tier": "auto",
  "stop": "string",
  "store": true,
  "stream_options": {
    "include_usage": true
  },
  "temperature": 0,
  "tool_choice": "none",
  "tools": [
    {
      "function": {
        "name": "string",
        "description": "string",
        "parameters": {},
        "strict": true
      },
      "type": "function"
    }
  ],
  "top_logprobs": 0,
  "top_p": 0,
  "user": "string",
  "web_search_options": {
    "search_context_size": "low",
    "user_location": {
      "approximate": {
        "city": "string",
        "country": "string",
        "region": "string",
        "timezone": "string"
      },
      "type": "approximate"
    }
  },
  "stream": false
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
GET
/chub/{model}/v1/models
Fetch the list of available models. Will only return the path's model.
Parameters
Name	Description
model *
string
(path)
	

Available values : mythomax, asha, soji, mixtral, mistral, mobile
Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "data": []
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
/{model}/v1/models
Fetch the list of available models. Will only return the path's model.
Parameters
Name	Description
model *
string
(path)
	

Available values : mythomax, asha, soji, mixtral, mistral, mobile
Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "data": []
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
/v1/chat/completions
OpenAI Mimic API endpoint for chat completions (Model ambiguous, Must be one in model list for this endpoint).
Parameters

No parameters
Request body

{
  "messages": [
    {
      "content": "string",
      "role": "developer",
      "name": "string"
    },
    {
      "content": "string",
      "role": "system",
      "name": "string"
    },
    {
      "content": "string",
      "role": "user",
      "name": "string"
    },
    {
      "role": "assistant",
      "audio": {
        "id": "string"
      },
      "content": "string",
      "function_call": {
        "arguments": "string",
        "name": "string"
      },
      "name": "string",
      "refusal": "string",
      "tool_calls": [
        {
          "id": "string",
          "function": {
            "arguments": "string",
            "name": "string"
          },
          "type": "function"
        }
      ]
    },
    {
      "content": "string",
      "role": "tool",
      "tool_call_id": "string"
    },
    {
      "content": "string",
      "name": "string",
      "role": "function"
    }
  ],
  "model": "string",
  "audio": {
    "format": "wav",
    "voice": "string"
  },
  "frequency_penalty": 0,
  "function_call": "none",
  "functions": [
    {
      "name": "string",
      "description": "string",
      "parameters": {}
    }
  ],
  "logit_bias": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  },
  "logprobs": true,
  "max_completion_tokens": 0,
  "max_tokens": 0,
  "metadata": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "modalities": [
    "text"
  ],
  "n": 0,
  "parallel_tool_calls": true,
  "prediction": {
    "content": "string",
    "type": "content"
  },
  "presence_penalty": 0,
  "reasoning_effort": "low",
  "response_format": {
    "type": "text"
  },
  "seed": 0,
  "service_tier": "auto",
  "stop": "string",
  "store": true,
  "stream_options": {
    "include_usage": true
  },
  "temperature": 0,
  "tool_choice": "none",
  "tools": [
    {
      "function": {
        "name": "string",
        "description": "string",
        "parameters": {},
        "strict": true
      },
      "type": "function"
    }
  ],
  "top_logprobs": 0,
  "top_p": 0,
  "user": "string",
  "web_search_options": {
    "search_context_size": "low",
    "user_location": {
      "approximate": {
        "city": "string",
        "country": "string",
        "region": "string",
        "timezone": "string"
      },
      "type": "approximate"
    }
  },
  "stream": false
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
GET
/v1/models
Fetch the list of all available models.
Parameters

No parameters
Responses
Code	Description	Links
200	

Successful Response
Media type
Controls Accept header.

{
  "data": []
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
