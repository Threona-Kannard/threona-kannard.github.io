import { useState } from 'react'

import './App.css'

function App() {
  
  return (
    <>
      <div className="relative">
        <div className="absolute inset-0 pointer-events-none overflow-hidden z-50">
          <div className="flex justify-center items-start">
            <div className="blob">
              <div className="gradient-pink"></div>
            </div>{" "}
            <div className="blob">
              <div className="gradient-green"></div>
            </div>{" "}
            <div className="blob">
              <div className="gradient-blue"></div>
            </div>
          </div>
        </div>
        <div className="relative">
          <div className="noise-bg absolute inset-0" aria-hidden="true">
            <svg>
              <filter id="noise-bg-fx">
                <feTurbulence baseFrequency="0.5"></feTurbulence>
              </filter>
            </svg>
          </div>
          <div className="min-h-screen flex flex-col justify-between">
            {/* <main>Hello</main> */}
          </div>
        </div>
      </div>
    </>
  )
}

export default App
