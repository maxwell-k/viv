VERSION ?= $(shell git describe --tags --always --dirty=-dev | sed 's/^v//g')

venv: ## generate environment
	pdm install

assets/viv-help.svg:
	FORCE_COLOR=1 viv --help | yartsu -t 'viv --help' -w 70 -o $@

.PHONY: dev-install
dev-install:
	ln -sf $(PWD)/src/viv/viv.py ~/.local/share/viv/viv.py

## docs |> update docs files
docs: docs/viv.py docs/index.md

docs/viv.py: src/viv/viv.py
	@cp $< $@

docs/index.md: README.md
	@printf -- '---\nhide: [navigation]\n---\n\n' > $@
	@cat $< >> $@

examples/black: .FORCE
	rm -f $@
	viv shim black -y -s -f -o $@

clean: ## remove build artifacts
	rm -rf {build,dist}

EXAMPLES = cli.py sys_path.py exe_specific.py frozen_import.py named_env.py scrape.py
generate-example-vivens: ##
	for f in $(EXAMPLES); \
		do python examples/$$f; done


.FORCE:
.PHONY: .FORCE
-include .task.cfg.mk
