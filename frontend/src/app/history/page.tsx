"use client";

import { useEffect, useState } from "react";

interface Note {
  id: number;
  video_id: string;
  video_url: string;
  created_at: string;
}

export default function HistoryPage() {
  const [notes, setNotes] = useState<Note[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchNotes();
  }, []);

  const fetchNotes = async () => {
    try {
      const res = await fetch(
        "http://127.0.0.1:8000/notes"
      );

      const data = await res.json();

      setNotes(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-8">
      <div className="max-w-5xl mx-auto">

        <h1 className="text-4xl font-bold mb-8">
          Notes History
        </h1>

        {loading ? (
          <p>Loading...</p>
        ) : (
          <div className="space-y-4">
            {notes.map((note) => (
              <div
                key={note.id}
                className="border rounded-lg p-4"
              >
                <p>
                  <strong>ID:</strong>{" "}
                  {note.id}
                </p>

                <p>
                  <strong>Video ID:</strong>{" "}
                  {note.video_id}
                </p>

                <p>
                  <strong>Created:</strong>{" "}
                  {new Date(
                    note.created_at
                  ).toLocaleString()}
                </p>
              </div>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
