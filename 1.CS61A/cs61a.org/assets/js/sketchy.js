// A little library that adds a sketching button to the nav bar.
// Once clicked, you can draw on a canvas on top of the page,
// and then click again to hide the canvas.

var makeSketchCanvas = function () {
  // Max canvas area (in pixels) before drawing is disabled
  // https://stackoverflow.com/questions/6081483/maximum-size-of-a-canvas-element
  const canvasMaxArea = 16e6;

  const activePointers = new Map();
  const lineColor = document.body.classList.contains("dark-mode-active") ? "white" : "black";

  // Create the canvas and bind events
  const canvasTop = $(document).scrollTop() - 500;
  const $canvas = $("<canvas>").css({
    cursor: "crosshair",
    // Start the canvas just above the scroll position
    // Otherwise the canvas gets too big and performance suffers
    top: canvasTop,
    left: 0,
    position: "absolute",
    zIndex: 99,
    backgroundColor: "transparent",
    backgroundColor: "rgba(0, 0, 0, 0.25)",
    userSelect: "none",
    pointerEvents: "none",
    display: "none"
  });

  const ctx = $canvas[0].getContext("2d");

  $("body").append($canvas);

  setCanvasHeight();

  // Helpful message about the end of the canvas
  ctx.font = "16px Arial";
  ctx.strokeStyle = "white";
  ctx.lineWidth = 3;
  ctx.fillStyle = "#996515";
  var reloadMsg = "Reload the page to sketch above this point.";
  ctx.strokeText(reloadMsg, 20, 20);
  ctx.fillText(reloadMsg, 20, 20);

  $canvas.on("pointermove", handlePointerEvent);
  $canvas.on("pointerdown", handlePointerEvent);
  $canvas.on("pointerup", handlePointerEvent);
  $canvas.on("pointerout", handlePointerEvent);
  $canvas.on("pointercancel", handlePointerEvent);

  // suppress touch scrolling
  $canvas.on("touchmove", handlePointerEvent);

  $(window).resize(setCanvasHeight);

  function setCanvasHeight() {
    var canvasWidth = window.innerWidth;
    // Add some blank space at the bottom of the page for sketching
    var desiredHeight = (document.body.clientHeight - canvasTop) + 500;

    // Capping necessary to prevent oversized canvases that exceed browser memory
    var maxHeight = Math.floor(canvasMaxArea / canvasWidth);
    var canvasHeight = Math.min(desiredHeight, maxHeight);

    // Fetch current data so we can repaint it after resizing
    var canvasData = ctx.getImageData(0, 0, canvasWidth, canvasHeight);
    // Actually resize the canvas
    $canvas.attr("width", canvasWidth).attr("height", canvasHeight);
    // Re-paint the old image data
    ctx.putImageData(canvasData, 0, 0);
  }

  function drawPoint(currX, currY) {
    ctx.beginPath();
    ctx.fillStyle = lineColor;
    ctx.fillRect(currX, currY, 2, 2);
    ctx.closePath();
  }

  function drawLine(prevX, prevY, currX, currY) {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = lineColor;
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.closePath();
  }

  function handlePointerEvent(event) {
    const pointerID = event.originalEvent.pointerId;
    switch (event.type) {
      case "pointerdown":
        const currX = event.pageX - $canvas.offset().left;
        const currY = event.pageY - $canvas.offset().top;
        drawPoint(currX, currY);
        activePointers.set(pointerID, [currX, currY]);
        break;
      case "pointermove":
        if (activePointers.has(pointerID)) {
          const [prevX, prevY] = activePointers.get(pointerID);
          const currX = event.pageX - $canvas.offset().left;
          const currY = event.pageY - $canvas.offset().top;
          drawLine(prevX, prevY, currX, currY);
          activePointers.set(pointerID, [currX, currY]);
        }
        break;
      case "pointerup":
      case "pointerout":
      case "pointercancel":
        activePointers.delete(pointerID);
        break;
    }
    event.preventDefault();
  }

  return $canvas;
};

var makeSketchButton = function () {
  var $canvas;
  var canvasOn = false;

  var activateButton = function () {
    $drawButton.find("span").css({
      "-webkit-filter": "grayscale(0%)",
      filter: "grayscale(0%)",
    });
  };
  var deactivateButton = function () {
    $drawButton.find("span").css({
      "-webkit-filter": "grayscale(100%)",
      filter: "grayscale(100%)",
    });
  };

  var toggleCanvas = function () {
    if (!$canvas) {
      $canvas = makeSketchCanvas();
    }

    if (canvasOn) {
      $canvas.hide();
      $canvas.css("pointerEvents", "none");
      deactivateButton();
    } else {
      $canvas.show();
      $canvas.css("pointerEvents", "auto");
      activateButton();
    }
    canvasOn = !canvasOn;
  };

  // Create the button and bind events
  var $drawButton = $("<button><span>✏️</span>")
    .attr("type", "button")
    .addClass("btn btn-primary")
    .css({
      float: "left",
      marginTop: 8,
    });
  deactivateButton();

  $drawButton.on("click", toggleCanvas);

  return $drawButton;
};

$(document).ready(function () {
  $(".navbar-header").append(makeSketchButton());
});
