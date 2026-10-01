import { useEffect, useState } from "react";

import Header from "./components/Header";
import Sidebar from "./components/Sidebar";

import Dashboard from "./pages/Dashboard";
import AttackSimulator from "./pages/AttackSimulator";
import Analytics from "./pages/Analytics";
import History from "./pages/History";

import {
  startSimulation,
  stopSimulation,
  getEvents,
  getSimulationStatus
} from "./services/api";


export default function App() {

  const [page, setPage] = useState("dashboard");

  const [events, setEvents] = useState([]);

  const [running, setRunning] = useState(false);

  const [connectionStatus, setConnectionStatus] =
    useState("CONNECTING");


  /*
  =========================
  LOAD EVENTS
  =========================
  */

  async function loadEvents() {

    try {

      const data = await getEvents(200);

      if (Array.isArray(data)) {
        setEvents(data);
      } else {
        setEvents([]);
      }

    } catch (error) {

      console.error(
        "Failed to load events:",
        error
      );

    }
  }


  /*
  =========================
  CHECK BACKEND
  =========================
  */

 async function checkSimulationStatus() {

  try {

    const status =
      await getSimulationStatus();

    console.log(
      "BACKEND STATUS RESPONSE:",
      status
    );

    setRunning(
      Boolean(status.running)
    );

    setConnectionStatus(
      "CONNECTED"
    );

  } catch (error) {

    console.error(
      "BACKEND CONNECTION ERROR:",
      error
    );

    setConnectionStatus(
      "OFFLINE"
    );

  }
}


  /*
  =========================
  INITIAL LOAD
  =========================
  */

  useEffect(() => {

    loadEvents();

    checkSimulationStatus();

    const interval =
      setInterval(() => {

        loadEvents();
        checkSimulationStatus();

      }, 2000);


    return () => {
      clearInterval(interval);
    };

  }, []);


  /*
  =========================
  START SIMULATION
  =========================
  */

  async function handleStart(attackType) {

    try {

      console.log(
        "Starting attack:",
        attackType
      );

      if (!attackType) {
        throw new Error(
          "Attack type was not provided."
        );
      }


      const result =
        await startSimulation(
          attackType
        );


      console.log(
        "Simulation response:",
        result
      );


      if (!result || result.success !== true) {

        throw new Error(
          result?.message ||
          "Simulation could not be started. " +
          "Another simulation may already be running."
        );

      }


      setRunning(true);

      setConnectionStatus(
        "CONNECTED"
      );


      /*
      Refresh database events
      */

      await loadEvents();


      /*
      Go to dashboard
      */

      setPage("dashboard");


    } catch (error) {

      console.error(
        "Start simulation error:",
        error
      );


      alert(
        "Unable to start simulation.\n\n" +
        error.message
      );

    }

  }


  /*
  =========================
  STOP SIMULATION
  =========================
  */

  async function handleStop() {

    try {

      console.log(
        "Stopping simulation..."
      );


      const result =
        await stopSimulation();


      console.log(
        "Stop response:",
        result
      );


      setRunning(false);


      await loadEvents();


    } catch (error) {

      console.error(
        "Stop simulation error:",
        error
      );


      alert(
        "Unable to stop simulation.\n\n" +
        error.message
      );

    }

  }


  /*
  =========================
  UI
  =========================
  */

  return (
    <div className="app">

      <Sidebar
        page={page}
        setPage={setPage}
      />


      <main className="main">

        <Header
          connectionStatus={
            connectionStatus
          }
        />


        {page === "dashboard" && (

          <Dashboard
            events={events}
            running={running}
            connectionStatus={
              connectionStatus
            }
          />

        )}


        {page === "simulator" && (

          <AttackSimulator
            onStart={handleStart}
            onStop={handleStop}
            running={running}
          />

        )}


        {page === "analytics" && (

          <Analytics
            events={events}
          />

        )}


        {page === "history" && (

          <History
            events={events}
          />

        )}

      </main>

    </div>
  );
}