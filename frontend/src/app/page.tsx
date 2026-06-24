"use client";
import { useState } from "react";

export default function Home() {
  const [youtubeUrl, setYoutubeUrl] = useState("");
  const [response, setResponse] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const generateNotes = async () => {
try {
setLoading(true);


const res = await fetch(
  "http://127.0.0.1:8000/generate-notes",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      youtube_url: youtubeUrl,
    }),
  }
);

console.log("Status:", res.status);

const text = await res.text();

console.log("Response Text:", text);

if (!res.ok) {
  throw new Error(
    `Backend Error ${res.status}: ${text}`
  );
}

const data = JSON.parse(text);

console.log("Parsed Data:", data);

setResponse(data);

} catch (error) {
console.error("Frontend Error:", error);

alert(
  error instanceof Error
    ? error.message
    : "Failed to generate notes"
);

} finally {
setLoading(false);
}
};


  return (
    <main className="min-h-screen py-12 px-4">
      <div className="max-w-5xl mx-auto">

        {/* Hero Section */}
        <div className="text-center mb-16">
          <div className="inline-flex items-center rounded-full border border-blue-200 bg-blue-50 px-4 py-2 text-sm font-medium text-blue-700 mb-6">
            AI Powered Learning Assistant
          </div>

          <h1 className="text-5xl md:text-6xl font-bold tracking-tight mb-6">
            Learn Faster From
            <span className="block text-blue-600">
              Any YouTube Video
            </span>
          </h1>

          <p className="text-lg md:text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            Generate executive summaries,
            detailed notes, and key takeaways
            instantly using AI.
          </p>
        </div>

        {/* Input Card */}
        <div className="bg-white/90 backdrop-blur-sm rounded-3xl shadow-xl border border-gray-100 p-8 mb-10">
          <div className="space-y-5">
            <input
              type="text"
              value={youtubeUrl}
              onChange={(e) =>
                setYoutubeUrl(e.target.value)
              }
              placeholder="Paste YouTube URL..."
              className="
                w-full
                rounded-2xl
                border
                border-gray-300
                p-5
                text-lg
                focus:outline-none
                focus:ring-2
                focus:ring-blue-500
                focus:border-blue-500
              "
            />

            <button
              onClick={generateNotes}
              disabled={loading}
              className="
                w-full
                rounded-2xl
                bg-blue-600
                text-white
                p-5
                text-lg
                font-semibold
                hover:bg-blue-700
                transition
                disabled:opacity-50
                disabled:cursor-not-allowed
              "
            >
              {loading
                ? "Generating Notes..."
                : "Generate Notes"}
            </button>
          </div>
        </div>

        {/* Results */}
        <div className="grid md:grid-cols-3 gap-6 mb-12">
  <div className="bg-white rounded-3xl shadow-lg p-6">
    <h3 className="text-lg font-bold mb-2">
      Executive Summary
    </h3>

    <p className="text-gray-600">
      Quickly understand the main ideas
      from any YouTube video.
    </p>
  </div>

  <div className="bg-white rounded-3xl shadow-lg p-6">
    <h3 className="text-lg font-bold mb-2">
      Detailed Notes
    </h3>

    <p className="text-gray-600">
      Get structured notes generated
      automatically using AI.
    </p>
  </div>

  <div className="bg-white rounded-3xl shadow-lg p-6">
    <h3 className="text-lg font-bold mb-2">
      Key Takeaways
    </h3>

    <p className="text-gray-600">
      Extract the most actionable insights
      in seconds.
    </p>
  </div>
</div>
        {response && (
          <div className="space-y-8">

            {/* Executive Summary */}
            <div className="bg-white rounded-3xl shadow-lg p-8">
              <h2 className="text-2xl font-bold mb-4">
                Executive Summary
              </h2>

              <p className="text-gray-700 leading-8">
                {response.executive_summary}
              </p>
            </div>

            {/* Detailed Notes */}
            <div className="bg-white rounded-3xl shadow-lg p-8">
              <h2 className="text-2xl font-bold mb-4">
                Detailed Notes
              </h2>

              <p className="text-gray-700 leading-8 whitespace-pre-wrap">
                {response.detailed_notes}
              </p>
            </div>

            {/* Key Takeaways */}
            <div className="bg-white rounded-3xl shadow-lg p-8">
              <h2 className="text-2xl font-bold mb-4">
                Key Takeaways
              </h2>

              <ul className="list-disc pl-6 space-y-3 text-gray-700">
                {response.key_takeaways?.map(
                  (
                    item: string,
                    index: number
                  ) => (
                    <li key={index}>
                      {item}
                    </li>
                  )
                )}
              </ul>
            </div>

          </div>
        )}
      </div>
    </main>
  );
}
