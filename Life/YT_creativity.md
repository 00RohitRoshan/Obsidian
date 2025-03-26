- Recreate Thumbnails 
- Checkout/search their source
- Check other videos previously made on that topic

#### YtGpt
anejnahsortihor@gmail.com
- Gemini `AIzaSyAbpLfeZtNU8ZCU9kfhQLWBZZYWpylEO8k`
- Pexels `13RJn1t7nVbVtwaSaHaxMFjjbxnPXimnyqYoSEP0hoY2uEpY7bXS6yQM`
- OpenAi `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`

Feature
- ✅ Fix Central Log
- ✅ Remove token limit / ❌ make it dynamic
- ✅ Check if JSON required from llm_completion
- ✅ *`Removed Timeout`* Error communicating with OpenAI: Request timed out. 
- ✅ Fixx Memmory usage [Apparently solved by batch job] 👇
- Skip Writing Blank frame in v.write_videofile / ✅ Directly write the clips then merge [DivideVideoInto1MinuteChunks] / change the times in the composition / trim using ffmpeg(still render those blank frame)
- ✅ fix `[vost#0:0/copy @ 0000014e521c9dc0] Non-monotonic DTS; previous: 11326629, current: 8567829; changing to 11326630. This may result in incorrect timestamps in the output file`
- ❌ group assets by their start and end time so the composition works properly [untill it generates long video good to go for tmplating , misallignment wrong order doesn't bother that much]
- 🟡 get synonyms of the search querr from GPT
- 🟡 get content from [stableDiffusion]/[OpenSora]/other
- 🟡 Cache URL from Pexel API
    - save file path
    - use
- 🟡 Cache Resources from Pexel API
    - downlod
    - save file path
    - use
- ✅ Checkout CoQuiTTS
- ✅ Merge CoQuiTTS and stable branch & SUNO
- 🟡 Local AI OLLAMA 
- 🟡 Create API to be able to invoke any specific step
- 🟡 [Templates](https://docs.shortgpt.ai/docs/getting-started) by making scripts and additional functionality
- 🟡 Make log nonblocking with correct funcname



#### Source
- Whitepaper  
- Exam syllabus  
- News/Trending  