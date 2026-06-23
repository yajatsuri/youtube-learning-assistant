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
      console.log("Headers:", [...res.headers.entries()]);

      const text = await res.text();

      console.log("Raw Response:", text);

      const data = JSON.parse(text);

      console.log("Parsed Response:", data);

      setResponse(data);

    } catch (error) {
      console.error(
        "Frontend Error:",
        error
      );

      alert(
        "Failed to generate notes"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-8 text-center">
          YouTube Learning Assistant
        </h1>

        <div className="space-y-4">
          <input
            type="text"
            value={youtubeUrl}
            onChange={(e) =>
              setYoutubeUrl(e.target.value)
            }
            placeholder="Paste YouTube URL..."
            className="w-full border rounded-lg p-4"
          />

          <button
            onClick={generateNotes}
            disabled={loading}
            className="w-full border rounded-lg p-4 font-semibold"
          >
            {loading
              ? "Generating..."
              : "Generate Notes"}
          </button>
        </div>

        {response && (
          <div className="mt-10 space-y-8">
            <div>
              <h2 className="text-2xl font-bold mb-2">
                Executive Summary
              </h2>
              <p>{response.executive_summary}</p>
            </div>

            <div>
              <h2 className="text-2xl font-bold mb-2">
                Detailed Notes
              </h2>
              <p>{response.detailed_notes}</p>
            </div>

            <div>
              <h2 className="text-2xl font-bold mb-2">
                Key Takeaways
              </h2>

              <ul className="list-disc pl-6">
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
