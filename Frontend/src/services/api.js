const API_BASE =
  import.meta.env.VITE_SIMULATOR_API ||
  "http://127.0.0.1:9000";

console.log(
  "SIMULATOR API:",
  API_BASE
);


async function request(endpoint, options = {}) {

  const url = `${API_BASE}${endpoint}`;

  console.log(
    "API REQUEST:",
    options.method || "GET",
    url
  );

  try {

    const response = await fetch(url, {
      method: options.method || "GET",
      headers: {
        ...(options.body
          ? { "Content-Type": "application/json" }
          : {})
      },
      ...(options.body
        ? { body: JSON.stringify(options.body) }
        : {})
    });


    console.log(
      "API RESPONSE:",
      response.status,
      response.statusText
    );


    const text =
      await response.text();


    let data;

    try {
      data = text
        ? JSON.parse(text)
        : {};
    } catch {
      data = {
        raw: text
      };
    }


    if (!response.ok) {

      throw new Error(
        `API ${response.status}: ${
          data?.detail ||
          data?.message ||
          text ||
          response.statusText
        }`
      );

    }


    return data;

  } catch (error) {

    console.error(
      "API FETCH ERROR:",
      error
    );

    throw error;

  }
}


/* =========================
   EVENTS
========================= */

export async function getEvents(
  limit = 100
) {

  return request(
    `/api/events?limit=${limit}`
  );

}


/* =========================
   START
========================= */

export async function startSimulation(
  attackType
) {

  if (!attackType) {
    throw new Error(
      "Attack type is required."
    );
  }


  return request(
    `/api/simulations/start/${encodeURIComponent(
      attackType
    )}`,
    {
      method: "POST"
    }
  );

}


/* =========================
   STOP
========================= */

export async function stopSimulation() {

  return request(
    "/api/simulations/stop",
    {
      method: "POST"
    }
  );

}


/* =========================
   STATUS
========================= */

export async function getSimulationStatus() {

  return request(
    "/api/simulations/status"
  );

}


/* =========================
   SCENARIOS
========================= */

export async function getScenarios() {

  return request(
    "/api/scenarios"
  );

}


/* =========================
   REPORT
========================= */

export async function getReportSummary() {

  return request(
    "/api/reports/summary"
  );

}


/* =========================
   REPLAY
========================= */

export async function getReplay(
  simulationId
) {

  if (!simulationId) {
    throw new Error(
      "Simulation ID is required."
    );
  }


  return request(
    `/api/replay/${encodeURIComponent(
      simulationId
    )}`
  );

}